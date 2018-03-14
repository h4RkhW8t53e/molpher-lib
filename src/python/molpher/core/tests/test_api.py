
# Copyright (c) 2016 Martin Sicho
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, sys
import unittest
from io import StringIO, BytesIO

from pkg_resources import resource_filename
from rdkit import Chem

from molpher import random
from molpher.core import ExplorationTree
from molpher.core import MolpherMol
from molpher.core import ExplorationData
from molpher.core import MolpherAtom
from molpher.core.morphing import AtomLibrary
from molpher.core.morphing import Molpher
from molpher.core.morphing.operators import *
from molpher.core.operations import *
from molpher.core.selectors import *

class TestPythonAPI(unittest.TestCase):
    
    def setUp(self):
        random.set_random_seed(42)
        self.test_source = 'CCO'
        self.test_target = 'C1=COC=C1'
        self.test_dir = os.path.abspath(resource_filename('molpher.core.tests', 'test_files/'))
        self.test_template_path = os.path.join(self.test_dir, 'test-template.xml')
        self.cymene_locked = os.path.join(self.test_dir, 'cymene.sdf')
        self.ethanol_locked = os.path.join(self.test_dir, 'ethanol.sdf')
        self.propanol = os.path.join(self.test_dir, 'propanol.sdf')
        self.remove_bond_test_mol = os.path.join(self.test_dir, 'remove_bond_test_mol.sdf')
        self.alanine = os.path.join(self.test_dir, 'alanine.sdf')
        self.isopropylphenol = os.path.join(self.test_dir, 'isopropylphenol.sdf')
        self.contract_bond_test_mol = os.path.join(self.test_dir, 'contract_bond_test_mol.sdf')
        self.reroute_test_mol = os.path.join(self.test_dir, 'reroute_test_mol.sdf')

    def tearDown(self):
        pass

    def testMolpherAtom(self):
        carbon = MolpherAtom("C")
        oxygen = MolpherAtom("O", -1)
        self.assertEqual(carbon.formal_charge, 0)
        carbon.formal_charge = 1
        self.assertEqual(carbon.formal_charge, 1)

        self.assertFalse(oxygen.is_locked or carbon.is_locked)

        oxygen.locking_mask = MolpherAtom.FULL_LOCK
        self.assertTrue(oxygen.is_locked)
        self.assertTrue(oxygen.lock_info['FULL_LOCK'])
        self.assertTrue(bool(oxygen.locking_mask & MolpherAtom.NO_ADDITION))
        self.assertTrue(bool(oxygen.locking_mask & MolpherAtom.KEEP_NEIGHBORS))
        self.assertTrue(bool(oxygen.locking_mask & MolpherAtom.NO_MUTATION))
        self.assertTrue(oxygen.lock_info['UNLOCKED'] == False)

        carbon.locking_mask = MolpherAtom.NO_MUTATION
        self.assertTrue(carbon.is_locked)
        self.assertFalse(carbon.lock_info['FULL_LOCK'])
        self.assertFalse(bool(carbon.locking_mask & MolpherAtom.NO_ADDITION))
        self.assertFalse(bool(carbon.locking_mask & MolpherAtom.KEEP_NEIGHBORS))
        self.assertTrue(bool(carbon.locking_mask & MolpherAtom.NO_MUTATION))
        self.assertTrue(carbon.lock_info['UNLOCKED'] == False)

    def testMolpherMol(self):
        mol = MolpherMol(self.test_target)
        mol.smiles = 'CCC'
        self.assertTrue('CCC')
        # mol.historic_descendents = ('CCC', 'CCCC')
        # self.assertEqual(('CCC', 'CCCC'), mol.historic_descendents)

        copy = mol.copy()
        copy.sascore = 0.54
        self.assertEqual(0.54, copy.sascore)
        self.assertEqual(0, mol.sascore)

        tree = ExplorationTree.create(source=mol.smiles, target='CCCNCCC')
        tree = ExplorationTree.create(source=mol, target='CCCNCCC')
        tree = ExplorationTree.create(source=mol, target=MolpherMol('CCCNCCC'))
        self.assertTrue(tree.hasMol(mol))
        def assign(x):
            tree.fetchMol(mol.smiles).smiles = x
        self.assertRaises(RuntimeError, assign, 'CCO')

        # atom locking stuff
        mol_locked = MolpherMol(self.cymene_locked)
        open_positions = (0, 2, 3, 9)
        for idx, atom in enumerate(mol_locked.atoms):
            if not atom.is_locked:
                self.assertIn(idx, open_positions)
            else:
                self.assertTrue(atom.lock_info['NO_ADDITION'])
                self.assertFalse(atom.lock_info['UNLOCKED'])
                self.assertFalse(atom.lock_info['FULL_LOCK'])

        # test RDKit conversion and locking information transfer
        rd_mol = mol_locked.asRDMol()
        output = StringIO()
        if sys.version_info[0] < 3:
            output = BytesIO()
        else:
            output = StringIO()
        writer = Chem.SDWriter(output)
        writer.write(rd_mol)
        writer.close()
        temp_path = self.test_dir + "/cymene_tmp.sdf"
        with open(temp_path, "w") as tempfile:
            tempfile.write(output.getvalue())
        new_cymene = MolpherMol(temp_path)
        os.remove(temp_path)
        for atm_old, atm_new in zip(mol_locked.atoms, new_cymene.atoms):
            self.assertTrue(atm_old.locking_mask == atm_new.locking_mask)

    def testAtomLibrary(self):
        smbls = ["O", "S"]
        my_lib = AtomLibrary(smbls)
        for x in my_lib.atoms:
            self.assertIn(x.symbol, smbls)

        default_lib = AtomLibrary.getDefaultLibrary()
        old_atoms = default_lib.atoms
        self.assertIn("C", [x.symbol for x in default_lib.atoms])

        AtomLibrary.setDefaultLibrary(my_lib)
        for x in default_lib.atoms:
            self.assertIn(x.symbol, smbls)

        for x in range(200):
            self.assertIn(default_lib.getRandomAtom().symbol, smbls)

        AtomLibrary.setDefaultLibrary(AtomLibrary(old_atoms)) # put everything back to default

    def assertOperatorValid(self, operator, test_mol, gens = 10):
        print("Testing operator:", operator)
        if not operator.getOriginal():
            self.assertRaises(RuntimeError, operator.setOriginal, None)
            self.assertRaises(RuntimeError, operator.morph)
        mol = MolpherMol(self.propanol)
        operator.setOriginal(mol)
        orig = operator.getOriginal()
        self.assertIsNotNone(orig)
        self.assertIsInstance(orig, MolpherMol)
        self.assertEqual(orig.getSMILES(), mol.getSMILES())

        operator.setOriginal(test_mol)
        for x in range(gens):
            mol = operator.morph()
            if mol:
                self.assertIsInstance(mol, MolpherMol)
                print(mol.smiles)
                operator.setOriginal(mol)


    def testAddAtomOperator(self):
        cymene_no_add = MolpherMol(self.cymene_locked)
        add_atom = AddAtom()
        self.assertOperatorValid(add_atom, cymene_no_add)

    def testAddBondOperator(self):
        propanol = MolpherMol(self.propanol)
        add_bond = AddBond()
        self.assertOperatorValid(add_bond, propanol)

        add_bond.setOriginal(propanol)
        open_bonds = add_bond.getOpenBonds()
        self.assertIsInstance(open_bonds, tuple)

    def testRemoveBondOperator(self):
        test_mol = MolpherMol(self.remove_bond_test_mol)
        remove_bond = RemoveBond()
        self.assertOperatorValid(remove_bond, test_mol)

        remove_bond.setOriginal(test_mol)
        open_bonds = remove_bond.getOpenBonds()
        self.assertIsInstance(open_bonds, tuple)

    def testMutateAtomOperator(self):
        self.assertOperatorValid(MutateAtom(), MolpherMol(self.isopropylphenol))

    def testInterlayAtomOperator(self):
        self.assertOperatorValid(InterlayAtom(), MolpherMol(self.isopropylphenol))

    def testRerouteBondOperator(self):
        self.assertOperatorValid(ContractBond(), MolpherMol(self.contract_bond_test_mol))

    def testContractBondOperator(self):
        self.assertOperatorValid(RerouteBond(), MolpherMol(self.reroute_test_mol))

    def testMolpher(self):
        cymene = MolpherMol(self.cymene_locked)

        operators = [AddAtom(), RemoveAtom()]
        molpher = Molpher(cymene, operators)
        molpher()
        morphs = molpher.getMorphs()
        self.assertTrue(morphs)
        self.assertFalse(molpher.getMorphs())

        morphs = []
        while len(morphs) < 50:
            morphs.append(molpher.next())
        self.assertEqual(50, len(morphs))

    def testMorphingOperator(self):
        class Identity(MorphingOperator):

            def setOriginal(self, mol):
                self.original = mol

            def morph(self):
                return self.original.copy()

        cymene = MolpherMol(self.cymene_locked)

        operators = [Identity()]
        molpher = Molpher(cymene, operators)
        molpher()
        for morph in molpher.getMorphs():
            self.assertEqual(morph.smiles, cymene.smiles)

    def testExplorationData(self):
        params = ExplorationData(
            source=self.test_source
            , target=self.test_target
        )

        params.operators = (OP_ADD_BOND, 'OP_REMOVE_BOND',)
        self.assertEqual(params.operators, ('OP_ADD_BOND', 'OP_REMOVE_BOND'))

        params.fingerprint = FP_EXT_ATOM_PAIRS
        self.assertEqual(params.fingerprint, 'FP_EXT_ATOM_PAIRS')
        params.fingerprint = 'FP_TOPOLOGICAL_LAYERED_2'
        self.assertEqual(params.fingerprint, 'FP_TOPOLOGICAL_LAYERED_2')
        params.similarity = 'SC_COSINE'
        self.assertEqual(params.similarity, 'SC_COSINE')
        params.similarity = SC_KULCZYNSKI
        self.assertEqual(params.similarity, 'SC_KULCZYNSKI')

        self.assertEqual(params.source.smiles, self.test_source)
        self.assertEqual(params.target.smiles, self.test_target)

        params.param_dict = {
            'target' : self.test_source
            , 'operators' : params.param_dict['operators'][:1]
        }
        self.assertEqual(params.target.smiles, self.test_source)
        self.assertEqual(params.operators, ('OP_ADD_BOND',))

        params_from_temp = ExplorationData.load(self.test_template_path)
        self.assertRaises(RuntimeError, lambda : ExplorationData.load('not/a/valid/path'))
        self.assertEqual(777, params_from_temp.far_produce)

    def testTree(self):
        mol1 = self.test_source
        mol2 = self.test_target
        params_dict = {
            'source' : mol1
            , 'target' : mol2
            , 'operators' : (OP_ADD_BOND, OP_REMOVE_BOND, OP_MUTATE_ATOM)
        }
        params = ExplorationData(**params_dict)


        self.assertRaises(AttributeError, lambda : ExplorationTree())
        tree_from_dict = ExplorationTree.create(tree_data=params_dict)
        tree_from_params = ExplorationTree.create(tree_data=params)
        tree_from_SMILES = ExplorationTree.create(source=mol1, target=mol2)
        def test_tree(tree):
            self.assertEqual(tree.params['source'], mol1)
            self.assertEqual(tree.params['target'], mol2)

        test_tree(tree_from_dict)
        test_tree(tree_from_params)
        test_tree(tree_from_SMILES)

        tree = tree_from_params

        # if we try to set source for non-empty tree, exception should be raised
        def func():
            tree.params = {
                'source' : mol2
                , 'target' : 'C'
            }
        self.assertRaises(RuntimeError, func)

        tree.thread_count = 1
        tree.params = {
            'target' : 'C'
        }
        self.assertEqual(1, tree.thread_count)
        self.assertEqual(tree.params['source'], mol1)
        self.assertEqual(tree.params['target'], 'C')
        self.assertEqual(tree.params['operators'], params.param_dict['operators']) # we should still have the same opers set

        tree.params = params; tree.thread_count = 0 # assign the original parameters back
        self.assertEqual(0, tree.thread_count)
        self.assertEqual(tree.params['source'], mol1)
        self.assertEqual(tree.params['target'], mol2)
        self.assertEqual(tree.params['operators'], params.param_dict['operators'])

        leaf = tree.leaves[0]
        self.assertRaises(RuntimeError, lambda : leaf.setSMILES('CCCC'))
        self.assertTrue(tree.hasMol(leaf))
        # self.assertEqual(tree, leaf.tree) # FIXME: add a reliable operator for comparison between trees
        leaf.setDistToTarget(0.5)
        self.assertEqual(tree.leaves[0].getDistToTarget(), 0.5)

        leaf_copy = tree.leaves[0].copy()
        # self.assertFalse(tree.hasMol(leaf_copy)) # FIXME: add a reliable operator for comparison between trees (this should check both the SMILES and the tree ownership)
        self.assertEqual(leaf_copy.getDistToTarget(), 0.5)
        leaf_copy.setDistToTarget(0.7)
        self.assertEqual(leaf.getDistToTarget(), 0.5)
        self.assertEqual(tree.leaves[0].getDistToTarget(), 0.5)
        self.assertEqual(leaf_copy.getDistToTarget(), 0.7)

    def testOperations(self):
        tree = ExplorationTree.create(tree_data={
            'source' : self.test_source
            , 'target' : self.test_target
        })

        iteration = [
            GenerateMorphsOper()
            , SortMorphsOper()
            , FilterMorphsOper()
            , ExtendTreeOper()
            , PruneTreeOper()
        ]

        for oper in iteration:
            self.assertRaises(RuntimeError, lambda : oper())

        fl = FindLeavesOper()
        for oper in iteration:
            tree.runOperation(oper)
        tree.runOperation(fl)
        for leaf1, leaf2, leaf3 in zip(sorted(fl.leaves), sorted(fl.tree.leaves), sorted(tree.leaves)):
            self.assertTrue(leaf1.smiles == leaf2.smiles == leaf3.smiles)

        tree.generateMorphs()
        tree.sortMorphs()
        previous = None
        for morph in tree.candidates:
            if previous:
                self.assertTrue(morph.dist_to_target >= previous)
                previous = morph.dist_to_target
            else:
                previous = morph.dist_to_target
        print([x.dist_to_target for x in tree.candidates])

        my_callback = lambda a, b : a.getDistToTarget() > b.getDistToTarget()
        my_sort = SortMorphsOper(tree, my_callback)
        my_sort()

        previous = None
        for morph in tree.candidates:
            if previous:
                self.assertTrue(morph.dist_to_target <= previous)
                previous = morph.dist_to_target
            else:
                previous = morph.dist_to_target
        print([x.dist_to_target for x in tree.candidates])

        tree.filterMorphs()
        selected = sum(tree.candidates_mask)
        clean_stuff = CleanMorphsOper()
        tree.runOperation(clean_stuff)
        self.assertEqual(len(tree.candidates), selected)

        tree.extend()

        callback = lambda x : sys.stdout.write(x.smiles + ' : ' + str(x.dist_to_target) + '\n')
        oper = TraverseOper(callback=callback)
        tree.runOperation(oper)

    def testMorphing(self):
        def callback(morph):
            callback.morphs_in_tree += 1
            self.assertTrue(morph)
            self.assertTrue(morph.tree)
            if morph.getItersWithoutDistImprovement() > 3:
                print('Callback output:')
                print(morph.getSMILES(), morph.getItersWithoutDistImprovement(), morph.getDistToTarget())
            if not callback.closest_mol:
                callback.closest_mol = morph
            current_dist = morph.getDistToTarget()
            min_dist = callback.closest_mol.getDistToTarget()
            if min_dist > current_dist:
                callback.closest_mol = morph
        callback.morphs_in_tree = 0
        callback.closest_mol = None

        class MorphingIteration(TreeOperation):

            parent = self

            def __init__(self, tree):
                super(MorphingIteration, self).__init__()
                self._tree = tree

            def __call__(self):
                print('Iteration: ', self._tree.getGenerationCount() + 1)
                self._tree.generateMorphs()
                for mol in self._tree.candidates:
                    self.parent.assertEqual(None, mol.tree)
                self._tree.filterMorphs()
                self._tree.extend()
                self._tree.prune()
                callback.morphs_in_tree = 0
                self._tree.traverse(callback)
                print('Number of morphs in the tree: ', callback.morphs_in_tree)
                print('Closest molecule to target: {0} -- distance: {1}'.format(
                    callback.closest_mol.getSMILES()
                    , callback.closest_mol.getDistToTarget()
                ))

            def getTree(self):
                return self._tree

            def setTree(self, tree):
                self._tree = tree

        tree = ExplorationTree.create(tree_data={
            'source' : self.test_source
            , 'target' : self.test_target
        })

        iterate = MorphingIteration(tree)
        counter = 0
        while counter < 5:
            iterate()
            counter += 1

        child = tree.leaves[0]
        self.assertTrue(child.tree)
        self.assertTrue(tree.hasMol(child))
        parent = child.getParentSMILES()
        tree.deleteSubtree(parent)
        self.assertFalse(tree.hasMol(parent))
        self.assertFalse(tree.hasMol(child))
        self.assertEqual(None, child.tree)
        self.assertEqual(parent, child.getParentSMILES())

        # check descendents
        def check_descs(morph):
            for desc_smiles in morph.descendents:
                desc = tree.fetchMol(desc_smiles)
                self.assertTrue(desc.tree)
        tree.traverse(check_descs)

if __name__ == "__main__":
    unittest.main()