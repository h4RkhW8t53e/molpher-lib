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

#ifndef EXPLORATIONTREE_HPP
#define	EXPLORATIONTREE_HPP

#include <memory>

#include "ExplorationData.hpp"
#include "operations/callbacks/TraverseCallback.hpp"
#include "operations/FilterMorphsOper.hpp"
#include "morphing/operators/MorphingOperator.hpp"
#include "morphing/MorphCollector.hpp"

class ExplorationTree 
#ifndef SWIG
: public std::enable_shared_from_this<ExplorationTree>
#endif
 {
    
    friend class TreeOperation;
    friend class FindLeavesOper;
    friend class GenerateMorphsOper;
    friend class SortMorphsOper;
    friend class FilterMorphsOper;
    friend class ExtendTreeOper;
    friend class PruneTreeOper;
    friend class TraverseOper;
    friend class CleanMorphsOper;

public:
    class ExplorationTreeImpl;
    
private:
    std::shared_ptr<ExplorationTreeImpl> pimpl;
    ExplorationTree();
    
public:
    
    static std::shared_ptr<ExplorationTree> create(const ExplorationData& data);
    static std::shared_ptr<ExplorationTree> create(const std::string& filename);
    static std::shared_ptr<ExplorationTree> create(const std::string& sourceMolAsSMILES, const std::string& targetMolAsSMILES);
    static std::shared_ptr<ExplorationTree> create(std::shared_ptr<MolpherMol> source, std::shared_ptr<MolpherMol> target);
    static std::shared_ptr<ExplorationTree> create(std::shared_ptr<MolpherMol> source);

    std::shared_ptr<ExplorationData> asData() const;
    void update(const ExplorationData& data);
    const std::vector<std::shared_ptr<MorphingOperator>>& getMorphingOperators();
    void setMorphingOperators(const std::vector<std::shared_ptr<MorphingOperator>>& operators);
    void addMorphingOperator(std::shared_ptr<MorphingOperator> operator_);
    
    void runOperation(TreeOperation& operation);
    
    std::vector<std::shared_ptr<MolpherMol> > fetchLeaves(bool increase_dist_improve_counter = false);
    std::shared_ptr<MolpherMol> fetchMol(const std::string& canonSMILES);
    bool hasMol(const std::string& canonSMILES);
    bool hasMol(std::shared_ptr<MolpherMol> mol);
    bool isPathFound();
    void deleteSubtree(const std::string& canonSMILES, bool descendents_only = false);
    void generateMorphs();
	void generateMorphs(const std::vector<std::shared_ptr<MorphCollector> >& collectors);
    void sortMorphs();
    void filterMorphs(bool verbose_output = false);
    void filterMorphs(FilterMorphsOper::MorphFilters filters, bool verbose_output = false);
    void extend();
    void prune();
    void traverse(const std::string& rootSMILES, TraverseCallback& callback);
    void traverse(TraverseCallback& callback);
    void save(const std::string& filename);
    
    int getThreadCount();
    unsigned getGenerationCount();
    std::vector<std::shared_ptr<MolpherMol> > getCandidateMorphs();
    std::vector<bool> getCandidateMorphsMask(); // TODO add a bitset version 
    
    void setThreadCount(int threadCnt);
    void setCandidateMorphsMask(const std::vector<bool>&); // TODO add a bitset version

};

#endif	/* EXPLORATIONTREE_HPP */

