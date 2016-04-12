
#include "data_structs/ExplorationData.hpp"
#include "core/data_structs/ExplorationDataImpl.hpp"
#include "core/data_structs/MolpherMolData.hpp"
#include "core/misc/inout.h"
#include "core/misc/iteration_serializer.hpp"

void MolpherMolToMolData(const MolpherMol& mol, MolpherMolData& data) {
    auto& descendants = mol.getDescendants();
    data.descendants.insert(descendants.begin(), descendants.end());
    data.historicDescendants = mol.getHistoricDescendants();
    data.SMILES = mol.getSMILES();
    data.distToTarget = mol.getDistToTarget();
    data.gensWithoutDistImprovement = mol.getItersWithoutDistImprovement();
    data.formula = mol.getFormula();
    data.molecularWeight = mol.getMolecularWeight();
    data.parentOper = mol.getParentOper();
    data.parentSmile = mol.getParentSMILES();
    data.sascore = mol.getSAScore();
}

MolpherMol* MolDataToMolpherMol(const MolpherMolData& data) {
    MolpherMol* mol = new MolpherMol(
            data.SMILES
            , data.formula
            , data.parentSmile
            , data.parentOper
            , data.distToTarget
            , data.distToTarget // dummy
            , data.molecularWeight
            , data.sascore
            );
    mol->setDescendants(data.historicDescendants);
    mol->setHistoricDescendants(data.historicDescendants);
    mol->setItersWithoutDistImprovement(data.gensWithoutDistImprovement);
    return mol;
}

ExplorationData::ExplorationData() : pimpl(new ExplorationData::ExplorationDataImpl()) {
    // no action
}

ExplorationData::~ExplorationData() = default;

void ExplorationData::addCandidate(const MolpherMol& mol) {
    if (!mol.isBoundToTree()) {
        MolpherMolData data;
        MolpherMolToMolData(mol, data);
        pimpl->candidates.push_back(data);
        pimpl->candidatesMask.push_back(true);
    } else {
        SynchCerr("The supplied molecule is bound to a tree. The data about the molecule "
                "will be copied, but the tree ownership information will be lost.");
    }
}

void ExplorationData::addCandidate(const MolpherMol& mol, unsigned index) {
    if (pimpl->candidates.size() - 1 >= index) {
        if (!mol.isBoundToTree()) {
            MolpherMolData data;
            MolpherMolToMolData(mol, data);
            pimpl->candidates.insert(pimpl->candidates.begin() + index, data);
            setCandidatesMaskAt(true, index);
        } else {
            SynchCerr("The supplied molecule is bound to a tree. The data about the molecule "
                "will be copied, but the tree ownership information will be lost.");
        }
    } else {
        throw std::runtime_error("Cannot add candidate. Index out of range.");
    }
}

void ExplorationData::addChemicalOperator(int oper) {
    auto& opers = pimpl->chemOpers;
    if (opers.find(oper) == opers.end()) {
        pimpl->chemOpers.insert(oper);
    } else {
        SynchCerr("Operator " + std::string(ChemOperLongDesc(oper)) + " already assigned.");
    }
}

void ExplorationData::addToDerivationMap(const std::string& smiles, unsigned derivation_count) {
    auto& derivations = pimpl->morphDerivations;
    if (derivations.find(smiles) == derivations.end()) {
        derivations.insert(std::make_pair(smiles, derivation_count));
    } else {
        derivations[smiles] = derivation_count;
    }
}

void ExplorationData::addToTreeMap(const std::string& smile, const MolpherMol& mol) {
    // TODO: add tree consistency check  + maybe add entry to derivation map for new entries?
    auto& map = pimpl->treeMap;
    MolpherMolData data;
    MolpherMolToMolData(mol, data);
    if (map.find(smile) == map.end()) {
        map.insert(std::make_pair(smile, data));
    } else {
        map[smile] = data;
    }
}

void ExplorationData::decreaseDerivationsCount(const std::string& smiles) {
    auto& derivations = pimpl->morphDerivations;
    if (derivations.find(smiles) == derivations.end()) {
        derivations[smiles]--;
    } else {
        throw std::runtime_error("Cannot decrease derivation counter for " + smiles 
                + ". Molecule is not present in the tree.");
    }
}

std::shared_ptr<std::vector<std::shared_ptr<MolpherMol> > > ExplorationData::getCandidates() const {
    auto ret = std::shared_ptr<std::vector<std::shared_ptr<MolpherMol> > >(
        new std::vector<std::shared_ptr<MolpherMol> >()
    );
    for (auto& item : pimpl->candidates) {
        MolpherMol* mol = MolDataToMolpherMol(item);
        ret->push_back(std::shared_ptr<MolpherMol>(mol));
    }
    return ret;
}

const std::vector<bool>& ExplorationData::getCandidatesMask() const {
    return pimpl->candidatesMask;
}

std::set<int> ExplorationData::getChemicalOperators() const {
    return pimpl->chemOpers;
}

int ExplorationData::getCntCandidatesToKeep() const {
    return pimpl->params.cntCandidatesToKeep;
}

int ExplorationData::getCntCandidatesToKeepMax() const {
    return pimpl->params.cntCandidatesToKeepMax;
}

int ExplorationData::getCntMaxMorphs() const {
    return pimpl->params.cntMaxMorphs;
}

int ExplorationData::getCntMorphs() const {
    return pimpl->params.cntMorphs;
}

int ExplorationData::getCntMorphsInDepth() const {
    return pimpl->params.cntMorphsInDepth;
}

const std::map<std::string, unsigned>& ExplorationData::getDerivationMap() const {
    return pimpl->morphDerivations;
}

double ExplorationData::getDistToTargetDepthSwitch() const {
    return pimpl->params.distToTargetDepthSwitch;
}

int ExplorationData::getFingerprint() const {
    return pimpl->fingerprint;
}

unsigned ExplorationData::getGenerationCount() const {
    return pimpl->generationCnt;
}

int ExplorationData::getItThreshold() const {
    return pimpl->params.itThreshold;
}

double ExplorationData::getMaxAcceptableMolecularWeight() const {
    return pimpl->params.maxAcceptableMolecularWeight;
}

double ExplorationData::getMinAcceptableMolecularWeight() const {
    return pimpl->params.minAcceptableMolecularWeight;
}

int ExplorationData::getSimilarityCoefficient() const {
    return pimpl->simCoeff;
}

std::shared_ptr<MolpherMol> ExplorationData::getSource() const {
    auto ret = std::shared_ptr<MolpherMol>(MolDataToMolpherMol(pimpl->source));
    return ret;
}

std::shared_ptr<MolpherMol> ExplorationData::getTarget() const {
    auto ret = std::shared_ptr<MolpherMol>(MolDataToMolpherMol(pimpl->target));
    return ret;
}

unsigned ExplorationData::getThreadCount() const {
    return pimpl->threadCnt;
}

std::shared_ptr<std::map<std::string, std::shared_ptr<MolpherMol> > > ExplorationData::getTreeMap() const {
    auto ret = std::shared_ptr<std::map<std::string, std::shared_ptr<MolpherMol> > >(
        new std::map<std::string, std::shared_ptr<MolpherMol> >()
    );
    for (auto& item : pimpl->treeMap) {
        MolpherMol* mol = MolDataToMolpherMol(item.second);
        ret->insert(
            std::make_pair(
                mol->getSMILES()
                , std::shared_ptr<MolpherMol>(mol)
            )
        );
    }
    return ret;
}

void ExplorationData::increaseDerivationsCount(const std::string& smiles) {
    auto& derivations = pimpl->morphDerivations;
    if (derivations.find(smiles) == derivations.end()) {
        derivations[smiles]++;
    } else {
        throw std::runtime_error("Cannot increase derivation counter for " + smiles 
                + ". Molecule is not present in the derivation map.");
    }
}

bool ExplorationData::isValid() const {
    return pimpl->isValid();
}

unsigned ExplorationData::popFromDerivationMap(const std::string& smiles) {
    auto& derivations = pimpl->morphDerivations;
    if (derivations.find(smiles) == derivations.end()) {
        unsigned ret = derivations[smiles];
        derivations.erase(smiles);
        return ret;
    } else {
        throw std::runtime_error("Cannot erase " + smiles 
                + ". Molecule is not present in the derivation map.");
    }
}

std::shared_ptr<MolpherMol> ExplorationData::popFromTreeMap(const std::string& smiles) {
    auto& tree = pimpl->treeMap;
    if (tree.find(smiles) != tree.end()) {
        auto ret = std::shared_ptr<MolpherMol>(MolDataToMolpherMol(tree.find(smiles)->second));
        tree.erase(smiles);
        return ret;
    } else {
        throw std::runtime_error("Cannot pop " + smiles 
                + ". Molecule is not present in the tree.");
    }
}

void ExplorationData::removeCandidate(unsigned index) {
    auto& candidates = pimpl->candidates;
    auto& mask = pimpl->candidatesMask;
    if (candidates.size() - 1 >= index) {
        candidates.erase(candidates.begin() + index);
        mask.erase(mask.begin() + index);
    } else {
        throw std::runtime_error("Cannot remove candidate. Index out of range.");
    }
}

void ExplorationData::setCandidatesMaskAt(bool val, unsigned index) {
    if (pimpl->candidatesMask.size() - 1 >= index) {
        pimpl->candidatesMask.insert(pimpl->candidatesMask.begin() + index, val);
    } else {
        throw std::runtime_error("Cannot value in mask. Index out of range.");
    }
}

void ExplorationData::removeChemicalOperator(int oper) {
    pimpl->chemOpers.erase(oper);
}

void ExplorationData::setCandidates(const std::vector<MolpherMol>& candidates) {
    pimpl->candidates.clear();
    pimpl->candidatesMask.clear();
    for (auto& mol : candidates) {
        MolpherMolData data;
        MolpherMolToMolData(mol, data);
        pimpl->candidates.push_back(data);
        pimpl->candidatesMask.push_back(true);
    }
}

void ExplorationData::setCandidatesMask(const std::vector<bool>& mask) {
    if (mask.size() == pimpl->candidates.size()) {
        pimpl->candidatesMask = mask;
    } else {
        throw std::runtime_error("Cannot set mask. The length of the mask does not match "
                "the number of candidates.");
    }
}

void ExplorationData::setChemicalOperators(const std::set<int>& opers) {
    pimpl->chemOpers = opers;
}

void ExplorationData::setCntCandidatesToKeep(int val) {
    pimpl->params.cntCandidatesToKeep = val;
}

void ExplorationData::setCntCandidatesToKeepMax(int val) {
    pimpl->params.cntCandidatesToKeepMax = val;
}

void ExplorationData::setCntMaxMorphs(int val) {
    pimpl->params.cntMaxMorphs = val;
}

void ExplorationData::setCntMorphs(int val) {
    pimpl->params.cntMorphs = val;
}

void ExplorationData::setCntMorphsInDepth(int val) {
    pimpl->params.cntMorphsInDepth = val;
}

void ExplorationData::setDistToTargetDepthSwitch(double val) {
    pimpl->params.distToTargetDepthSwitch = val;
}

void ExplorationData::setFingerprint(int val) {
    pimpl->fingerprint = val;
}

void ExplorationData::setGenerationCount(unsigned val) {
    pimpl->generationCnt = val;
}

void ExplorationData::setItThreshold(int val) {
    pimpl->params.itThreshold = val;
}

void ExplorationData::setMaxAcceptableMolecularWeight(double val) {
    pimpl->params.maxAcceptableMolecularWeight = val;
}

void ExplorationData::setMinAcceptableMolecularWeight(double val) {
    pimpl->params.minAcceptableMolecularWeight = val;
}

void ExplorationData::setSimilarityCoefficient(int val) {
    pimpl->simCoeff = val;
}

void ExplorationData::setSource(const MolpherMol& mol) {
    if (pimpl->treeMap.empty()) {
        MolpherMolData data;
        MolpherMolToMolData(mol, data);
        pimpl->source = data;
        pimpl->treeMap.insert(std::make_pair(data.SMILES, data));
    } else {
        throw std::runtime_error("Cannot set a source molecule for non-empty tree data.");
    }
}

void ExplorationData::setTarget(const MolpherMol& mol) {
    MolpherMolData data;
    MolpherMolToMolData(mol, data);
    pimpl->target = data;
}

void ExplorationData::setThreadCount(unsigned val) {
    pimpl->threadCnt = val;
}

std::shared_ptr<ExplorationData> ExplorationData::load(const std::string& file) {
    auto data = std::make_shared<ExplorationData>();
    molpher::iteration::IterationSerializer::load(file, *(data->pimpl));
    data->pimpl->treeMap.insert(std::make_pair(data->pimpl->source.SMILES, data->pimpl->source));
    return data;
}

void ExplorationData::save(const std::string& file) {
    molpher::iteration::IterationSerializer::save(file, *pimpl);
}