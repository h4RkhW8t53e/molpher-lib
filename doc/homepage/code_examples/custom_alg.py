from molpher.core import ExplorationTree as ETree
from molpher.algorithms.functions import find_path

cocaine = 'CN1C2CCC1C(C(=O)OC)C(OC(=O)c1ccccc1)C2'
procaine = 'O=C(OCCN(CC)CC)c1ccc(N)cc1'

tree = ETree.create(source=cocaine, target=procaine) # create the tree
counter = 0
while not tree.path_found:
    counter+=1
    print("Iteration", counter)
    tree.generateMorphs() # generate the first generation of morphs
    tree.sortMorphs() # sort morphs according to their distance to target (ascending)
    tree.filterMorphs() # remove molecules that do not meet certain criteria
    tree.extend() # connect the remaining molecules to the exploration tree
    tree.prune() # remove branches of the tree that do not converge

as_mol_grid(tree.fetchPathTo(tree.params['target']))