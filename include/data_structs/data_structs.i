/*
 Copyright (c) 2016 Martin Šícho

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

// MolpherAtom wrapper
%ignore MolpherAtom::operator=(const MolpherAtom&);
%ignore MolpherAtom::asRDAtom() const;
%ignore MolpherAtom::MolpherAtom(RDKit::Atom* atom);
%include "MolpherAtom.hpp"

// MoplherMol wrapper
%ignore MolpherMol::operator=(const MolpherMol&);
%ignore MolpherMol::MolpherMol(RDKit::ROMol* rd_mol);
%ignore MolpherMol::MolpherMol(RDKit::RWMol*& rd_mol);
%ignore MolpherMol::asRDMol(bool include_locks = false) const;
%catches(std::runtime_error) MolpherMol::setOwner(std::shared_ptr<ExplorationTree> tree);
%catches(std::runtime_error) MolpherMol::setSMILES(const std::string& smiles);
%catches(std::runtime_error) MolpherMol::setParentSMILES(const std::string& smiles);
%include "MolpherMol.hpp"

// ExplorationData wrapper
%catches(std::runtime_error) ExplorationData::load(const std::string& file);
%catches(std::runtime_error) ExplorationData::save(const std::string& file);
%catches(std::runtime_error) ExplorationData::setSource(const MolpherMol& mol);
%catches(std::runtime_error) ExplorationData::setCandidatesMask(const std::vector<bool>& mask);
%include "ExplorationData.hpp"

// ExplorationTree wrapper
%catches(std::runtime_error) ExplorationTree::update(const ExplorationData& data);
%catches(std::runtime_error) ExplorationTree::fetchMol(const std::string& canonSMILES);
%catches(std::runtime_error) ExplorationTree::deleteSubtree(const std::string& canonSMILES, bool descendents_only);
%include "ExplorationTree.hpp";
