# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_core', [dirname(__file__)])
        except ImportError:
            import _core
            return _core
        if fp is not None:
            try:
                _mod = imp.load_module('_core', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _core = swig_import_helper()
    del swig_import_helper
else:
    import _core
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _core.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _core.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _core.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _core.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _core.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _core.SwigPyIterator_equal(self, x)

    def copy(self):
        return _core.SwigPyIterator_copy(self)

    def next(self):
        return _core.SwigPyIterator_next(self)

    def __next__(self):
        return _core.SwigPyIterator___next__(self)

    def previous(self):
        return _core.SwigPyIterator_previous(self)

    def advance(self, n):
        return _core.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _core.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _core.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _core.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _core.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _core.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _core.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _core.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class SAScore(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SAScore, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SAScore, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["getInstance"] = lambda x: _core.SAScore_getInstance
    if _newclass:
        getInstance = staticmethod(_core.SAScore_getInstance)
    __swig_getmethods__["destroyInstance"] = lambda x: _core.SAScore_destroyInstance
    if _newclass:
        destroyInstance = staticmethod(_core.SAScore_destroyInstance)
    __swig_destroy__ = _core.delete_SAScore
    __del__ = lambda self: None

    def getScore(self, mol):
        return _core.SAScore_getScore(self, mol)
    __swig_getmethods__["loadData"] = lambda x: _core.SAScore_loadData
    if _newclass:
        loadData = staticmethod(_core.SAScore_loadData)
SAScore_swigregister = _core.SAScore_swigregister
SAScore_swigregister(SAScore)

def SAScore_getInstance():
    return _core.SAScore_getInstance()
SAScore_getInstance = _core.SAScore_getInstance

def SAScore_destroyInstance():
    return _core.SAScore_destroyInstance()
SAScore_destroyInstance = _core.SAScore_destroyInstance

def SAScore_loadData(*args):
    return _core.SAScore_loadData(*args)
SAScore_loadData = _core.SAScore_loadData


def run_path_finder(storagePath, jobFile, threadCnt):
    return _core.run_path_finder(storagePath, jobFile, threadCnt)
run_path_finder = _core.run_path_finder
class TreeOperation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TreeOperation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TreeOperation, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        if self.__class__ == TreeOperation:
            _self = None
        else:
            _self = self
        this = _core.new_TreeOperation(_self, *args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_TreeOperation
    __del__ = lambda self: None

    def __call__(self):
        return _core.TreeOperation___call__(self)

    def getTree(self):
        return _core.TreeOperation_getTree(self)

    def setTree(self, arg2):
        return _core.TreeOperation_setTree(self, arg2)
    def __disown__(self):
        self.this.disown()
        _core.disown_TreeOperation(self)
        return weakref_proxy(self)
TreeOperation_swigregister = _core.TreeOperation_swigregister
TreeOperation_swigregister(TreeOperation)

class FindLeavesOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FindLeavesOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FindLeavesOper, name)
    __repr__ = _swig_repr

    def __init__(self, expTree, increment_iters_without_dist_improve):
        this = _core.new_FindLeavesOper(expTree, increment_iters_without_dist_improve)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __call__(self):
        return _core.FindLeavesOper___call__(self)
    __swig_destroy__ = _core.delete_FindLeavesOper
    __del__ = lambda self: None
FindLeavesOper_swigregister = _core.FindLeavesOper_swigregister
FindLeavesOper_swigregister(FindLeavesOper)

class GenerateMoprhsOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GenerateMoprhsOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GenerateMoprhsOper, name)
    __repr__ = _swig_repr

    def __init__(self, expTree):
        this = _core.new_GenerateMoprhsOper(expTree)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __call__(self):
        return _core.GenerateMoprhsOper___call__(self)
    __swig_destroy__ = _core.delete_GenerateMoprhsOper
    __del__ = lambda self: None
GenerateMoprhsOper_swigregister = _core.GenerateMoprhsOper_swigregister
GenerateMoprhsOper_swigregister(GenerateMoprhsOper)

class SortMoprhsOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SortMoprhsOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SortMoprhsOper, name)
    __repr__ = _swig_repr

    def __init__(self, expTree):
        this = _core.new_SortMoprhsOper(expTree)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __call__(self):
        return _core.SortMoprhsOper___call__(self)
    __swig_destroy__ = _core.delete_SortMoprhsOper
    __del__ = lambda self: None
SortMoprhsOper_swigregister = _core.SortMoprhsOper_swigregister
SortMoprhsOper_swigregister(SortMoprhsOper)

class FilterMorphsOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FilterMorphsOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FilterMorphsOper, name)
    __repr__ = _swig_repr
    PROBABILITY = _core.FilterMorphsOper_PROBABILITY
    WEIGHT = _core.FilterMorphsOper_WEIGHT
    SYNTHESIS = _core.FilterMorphsOper_SYNTHESIS
    MAX_DERIVATIONS = _core.FilterMorphsOper_MAX_DERIVATIONS
    DUPLICATES = _core.FilterMorphsOper_DUPLICATES
    HISTORIC_DESCENDENTS = _core.FilterMorphsOper_HISTORIC_DESCENDENTS
    ALL = _core.FilterMorphsOper_ALL

    def __init__(self, *args):
        this = _core.new_FilterMorphsOper(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __call__(self):
        return _core.FilterMorphsOper___call__(self)
    __swig_destroy__ = _core.delete_FilterMorphsOper
    __del__ = lambda self: None
FilterMorphsOper_swigregister = _core.FilterMorphsOper_swigregister
FilterMorphsOper_swigregister(FilterMorphsOper)

class ExtendTreeOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ExtendTreeOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ExtendTreeOper, name)
    __repr__ = _swig_repr

    def __init__(self, expTree):
        this = _core.new_ExtendTreeOper(expTree)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __call__(self):
        return _core.ExtendTreeOper___call__(self)
    __swig_destroy__ = _core.delete_ExtendTreeOper
    __del__ = lambda self: None
ExtendTreeOper_swigregister = _core.ExtendTreeOper_swigregister
ExtendTreeOper_swigregister(ExtendTreeOper)

class PruneTreeOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PruneTreeOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PruneTreeOper, name)
    __repr__ = _swig_repr

    def __init__(self, expTree):
        this = _core.new_PruneTreeOper(expTree)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __call__(self):
        return _core.PruneTreeOper___call__(self)
    __swig_destroy__ = _core.delete_PruneTreeOper
    __del__ = lambda self: None
PruneTreeOper_swigregister = _core.PruneTreeOper_swigregister
PruneTreeOper_swigregister(PruneTreeOper)

class TraverseOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TraverseOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TraverseOper, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _core.new_TraverseOper(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __call__(self):
        return _core.TraverseOper___call__(self)
    __swig_destroy__ = _core.delete_TraverseOper
    __del__ = lambda self: None
TraverseOper_swigregister = _core.TraverseOper_swigregister
TraverseOper_swigregister(TraverseOper)

class TraverseCallback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TraverseCallback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TraverseCallback, name)
    __repr__ = _swig_repr

    def __init__(self):
        if self.__class__ == TraverseCallback:
            _self = None
        else:
            _self = self
        this = _core.new_TraverseCallback(_self, )
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_TraverseCallback
    __del__ = lambda self: None

    def processMorph(self, morph):
        return _core.TraverseCallback_processMorph(self, morph)
    def __disown__(self):
        self.this.disown()
        _core.disown_TraverseCallback(self)
        return weakref_proxy(self)
TraverseCallback_swigregister = _core.TraverseCallback_swigregister
TraverseCallback_swigregister(TraverseCallback)

class StringSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringSet, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _core.StringSet_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _core.StringSet___nonzero__(self)

    def __bool__(self):
        return _core.StringSet___bool__(self)

    def __len__(self):
        return _core.StringSet___len__(self)

    def append(self, x):
        return _core.StringSet_append(self, x)

    def __contains__(self, x):
        return _core.StringSet___contains__(self, x)

    def __getitem__(self, i):
        return _core.StringSet___getitem__(self, i)

    def add(self, x):
        return _core.StringSet_add(self, x)

    def discard(self, x):
        return _core.StringSet_discard(self, x)

    def __init__(self, *args):
        this = _core.new_StringSet(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def empty(self):
        return _core.StringSet_empty(self)

    def size(self):
        return _core.StringSet_size(self)

    def clear(self):
        return _core.StringSet_clear(self)

    def swap(self, v):
        return _core.StringSet_swap(self, v)

    def count(self, x):
        return _core.StringSet_count(self, x)

    def begin(self):
        return _core.StringSet_begin(self)

    def end(self):
        return _core.StringSet_end(self)

    def rbegin(self):
        return _core.StringSet_rbegin(self)

    def rend(self):
        return _core.StringSet_rend(self)

    def erase(self, *args):
        return _core.StringSet_erase(self, *args)

    def find(self, x):
        return _core.StringSet_find(self, x)

    def lower_bound(self, x):
        return _core.StringSet_lower_bound(self, x)

    def upper_bound(self, x):
        return _core.StringSet_upper_bound(self, x)

    def equal_range(self, x):
        return _core.StringSet_equal_range(self, x)

    def insert(self, __x):
        return _core.StringSet_insert(self, __x)
    __swig_destroy__ = _core.delete_StringSet
    __del__ = lambda self: None
StringSet_swigregister = _core.StringSet_swigregister
StringSet_swigregister(StringSet)

class MolpherMol(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MolpherMol, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MolpherMol, name)
    __repr__ = _swig_repr

    def __init__(self, other):
        this = _core.new_MolpherMol(other)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_MolpherMol
    __del__ = lambda self: None

    def fetchMolpherMolecule(self):
        return _core.MolpherMol_fetchMolpherMolecule(self)

    def isBound(self):
        return _core.MolpherMol_isBound(self)

    def copy(self):
        return _core.MolpherMol_copy(self)

    def getSMILES(self):
        return _core.MolpherMol_getSMILES(self)

    def getDistToTarget(self):
        return _core.MolpherMol_getDistToTarget(self)

    def getParentSMILES(self):
        return _core.MolpherMol_getParentSMILES(self)

    def getDescendants(self):
        return _core.MolpherMol_getDescendants(self)

    def getHistoricDescendants(self):
        return _core.MolpherMol_getHistoricDescendants(self)

    def getItersWithoutDistImprovement(self):
        return _core.MolpherMol_getItersWithoutDistImprovement(self)

    def getSAScore(self):
        return _core.MolpherMol_getSAScore(self)

    def getMolecularWeight(self):
        return _core.MolpherMol_getMolecularWeight(self)

    def setDistToTarget(self, dist):
        return _core.MolpherMol_setDistToTarget(self, dist)

    def setSAScore(self, score):
        return _core.MolpherMol_setSAScore(self, score)
MolpherMol_swigregister = _core.MolpherMol_swigregister
MolpherMol_swigregister(MolpherMol)

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _core.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _core.StringVector___nonzero__(self)

    def __bool__(self):
        return _core.StringVector___bool__(self)

    def __len__(self):
        return _core.StringVector___len__(self)

    def pop(self):
        return _core.StringVector_pop(self)

    def __getslice__(self, i, j):
        return _core.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _core.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _core.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _core.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _core.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _core.StringVector___setitem__(self, *args)

    def append(self, x):
        return _core.StringVector_append(self, x)

    def empty(self):
        return _core.StringVector_empty(self)

    def size(self):
        return _core.StringVector_size(self)

    def clear(self):
        return _core.StringVector_clear(self)

    def swap(self, v):
        return _core.StringVector_swap(self, v)

    def get_allocator(self):
        return _core.StringVector_get_allocator(self)

    def begin(self):
        return _core.StringVector_begin(self)

    def end(self):
        return _core.StringVector_end(self)

    def rbegin(self):
        return _core.StringVector_rbegin(self)

    def rend(self):
        return _core.StringVector_rend(self)

    def pop_back(self):
        return _core.StringVector_pop_back(self)

    def erase(self, *args):
        return _core.StringVector_erase(self, *args)

    def __init__(self, *args):
        this = _core.new_StringVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _core.StringVector_push_back(self, x)

    def front(self):
        return _core.StringVector_front(self)

    def back(self):
        return _core.StringVector_back(self)

    def assign(self, n, x):
        return _core.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _core.StringVector_resize(self, *args)

    def insert(self, *args):
        return _core.StringVector_insert(self, *args)

    def reserve(self, n):
        return _core.StringVector_reserve(self, n)

    def capacity(self):
        return _core.StringVector_capacity(self)
    __swig_destroy__ = _core.delete_StringVector
    __del__ = lambda self: None
StringVector_swigregister = _core.StringVector_swigregister
StringVector_swigregister(StringVector)

class ExplorationParameters(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ExplorationParameters, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ExplorationParameters, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _core.new_ExplorationParameters(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def valid(self):
        return _core.ExplorationParameters_valid(self)

    def getSourceMol(self):
        return _core.ExplorationParameters_getSourceMol(self)

    def getTargetMol(self):
        return _core.ExplorationParameters_getTargetMol(self)

    def getChemOperators(self):
        return _core.ExplorationParameters_getChemOperators(self)

    def getFingerprint(self):
        return _core.ExplorationParameters_getFingerprint(self)

    def getSimilarityCoef(self):
        return _core.ExplorationParameters_getSimilarityCoef(self)

    def getMinAcceptableMolecularWeight(self):
        return _core.ExplorationParameters_getMinAcceptableMolecularWeight(self)

    def getMaxAcceptableMolecularWeight(self):
        return _core.ExplorationParameters_getMaxAcceptableMolecularWeight(self)

    def getCntCandidatesToKeep(self):
        return _core.ExplorationParameters_getCntCandidatesToKeep(self)

    def getCntCandidatesToKeepMax(self):
        return _core.ExplorationParameters_getCntCandidatesToKeepMax(self)

    def getCntMorphs(self):
        return _core.ExplorationParameters_getCntMorphs(self)

    def getCntMorphsInDepth(self):
        return _core.ExplorationParameters_getCntMorphsInDepth(self)

    def getDistToTargetDepthSwitch(self):
        return _core.ExplorationParameters_getDistToTargetDepthSwitch(self)

    def getCntMaxMorphs(self):
        return _core.ExplorationParameters_getCntMaxMorphs(self)

    def getItThreshold(self):
        return _core.ExplorationParameters_getItThreshold(self)

    def setSourceMol(self, *args):
        return _core.ExplorationParameters_setSourceMol(self, *args)

    def setTargetMol(self, *args):
        return _core.ExplorationParameters_setTargetMol(self, *args)

    def setChemOperators(self, choices):
        return _core.ExplorationParameters_setChemOperators(self, choices)

    def setFingerprint(self, fp):
        return _core.ExplorationParameters_setFingerprint(self, fp)

    def setSimilarityCoef(self, coef):
        return _core.ExplorationParameters_setSimilarityCoef(self, coef)

    def setMinAcceptableMolecularWeight(self, weight):
        return _core.ExplorationParameters_setMinAcceptableMolecularWeight(self, weight)

    def setMaxAcceptableMolecularWeight(self, weight):
        return _core.ExplorationParameters_setMaxAcceptableMolecularWeight(self, weight)

    def setCntCandidatesToKeep(self, value):
        return _core.ExplorationParameters_setCntCandidatesToKeep(self, value)

    def setCntCandidatesToKeepMax(self, value):
        return _core.ExplorationParameters_setCntCandidatesToKeepMax(self, value)

    def setCntMorphs(self, value):
        return _core.ExplorationParameters_setCntMorphs(self, value)

    def setCntMorphsInDepth(self, value):
        return _core.ExplorationParameters_setCntMorphsInDepth(self, value)

    def setDistToTargetDepthSwitch(self, value):
        return _core.ExplorationParameters_setDistToTargetDepthSwitch(self, value)

    def setCntMaxMorphs(self, value):
        return _core.ExplorationParameters_setCntMaxMorphs(self, value)

    def setItThreshold(self, value):
        return _core.ExplorationParameters_setItThreshold(self, value)
    __swig_destroy__ = _core.delete_ExplorationParameters
    __del__ = lambda self: None
ExplorationParameters_swigregister = _core.ExplorationParameters_swigregister
ExplorationParameters_swigregister(ExplorationParameters)

class ExplorationTreeSnapshot(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ExplorationTreeSnapshot, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ExplorationTreeSnapshot, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["load"] = lambda x: _core.ExplorationTreeSnapshot_load
    if _newclass:
        load = staticmethod(_core.ExplorationTreeSnapshot_load)

    def save(self, filename):
        return _core.ExplorationTreeSnapshot_save(self, filename)
    __swig_destroy__ = _core.delete_ExplorationTreeSnapshot
    __del__ = lambda self: None
ExplorationTreeSnapshot_swigregister = _core.ExplorationTreeSnapshot_swigregister
ExplorationTreeSnapshot_swigregister(ExplorationTreeSnapshot)

def ExplorationTreeSnapshot_load(filename):
    return _core.ExplorationTreeSnapshot_load(filename)
ExplorationTreeSnapshot_load = _core.ExplorationTreeSnapshot_load

class MolpherMolVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MolpherMolVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MolpherMolVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _core.MolpherMolVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _core.MolpherMolVector___nonzero__(self)

    def __bool__(self):
        return _core.MolpherMolVector___bool__(self)

    def __len__(self):
        return _core.MolpherMolVector___len__(self)

    def pop(self):
        return _core.MolpherMolVector_pop(self)

    def __getslice__(self, i, j):
        return _core.MolpherMolVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _core.MolpherMolVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _core.MolpherMolVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _core.MolpherMolVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _core.MolpherMolVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _core.MolpherMolVector___setitem__(self, *args)

    def append(self, x):
        return _core.MolpherMolVector_append(self, x)

    def empty(self):
        return _core.MolpherMolVector_empty(self)

    def size(self):
        return _core.MolpherMolVector_size(self)

    def clear(self):
        return _core.MolpherMolVector_clear(self)

    def swap(self, v):
        return _core.MolpherMolVector_swap(self, v)

    def get_allocator(self):
        return _core.MolpherMolVector_get_allocator(self)

    def begin(self):
        return _core.MolpherMolVector_begin(self)

    def end(self):
        return _core.MolpherMolVector_end(self)

    def rbegin(self):
        return _core.MolpherMolVector_rbegin(self)

    def rend(self):
        return _core.MolpherMolVector_rend(self)

    def pop_back(self):
        return _core.MolpherMolVector_pop_back(self)

    def erase(self, *args):
        return _core.MolpherMolVector_erase(self, *args)

    def __init__(self, *args):
        this = _core.new_MolpherMolVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _core.MolpherMolVector_push_back(self, x)

    def front(self):
        return _core.MolpherMolVector_front(self)

    def back(self):
        return _core.MolpherMolVector_back(self)

    def assign(self, n, x):
        return _core.MolpherMolVector_assign(self, n, x)

    def resize(self, *args):
        return _core.MolpherMolVector_resize(self, *args)

    def insert(self, *args):
        return _core.MolpherMolVector_insert(self, *args)

    def reserve(self, n):
        return _core.MolpherMolVector_reserve(self, n)

    def capacity(self):
        return _core.MolpherMolVector_capacity(self)
    __swig_destroy__ = _core.delete_MolpherMolVector
    __del__ = lambda self: None
MolpherMolVector_swigregister = _core.MolpherMolVector_swigregister
MolpherMolVector_swigregister(MolpherMolVector)

class BoolVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BoolVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BoolVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _core.BoolVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _core.BoolVector___nonzero__(self)

    def __bool__(self):
        return _core.BoolVector___bool__(self)

    def __len__(self):
        return _core.BoolVector___len__(self)

    def pop(self):
        return _core.BoolVector_pop(self)

    def __getslice__(self, i, j):
        return _core.BoolVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _core.BoolVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _core.BoolVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _core.BoolVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _core.BoolVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _core.BoolVector___setitem__(self, *args)

    def append(self, x):
        return _core.BoolVector_append(self, x)

    def empty(self):
        return _core.BoolVector_empty(self)

    def size(self):
        return _core.BoolVector_size(self)

    def clear(self):
        return _core.BoolVector_clear(self)

    def swap(self, v):
        return _core.BoolVector_swap(self, v)

    def get_allocator(self):
        return _core.BoolVector_get_allocator(self)

    def begin(self):
        return _core.BoolVector_begin(self)

    def end(self):
        return _core.BoolVector_end(self)

    def rbegin(self):
        return _core.BoolVector_rbegin(self)

    def rend(self):
        return _core.BoolVector_rend(self)

    def pop_back(self):
        return _core.BoolVector_pop_back(self)

    def erase(self, *args):
        return _core.BoolVector_erase(self, *args)

    def __init__(self, *args):
        this = _core.new_BoolVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _core.BoolVector_push_back(self, x)

    def front(self):
        return _core.BoolVector_front(self)

    def back(self):
        return _core.BoolVector_back(self)

    def assign(self, n, x):
        return _core.BoolVector_assign(self, n, x)

    def resize(self, *args):
        return _core.BoolVector_resize(self, *args)

    def insert(self, *args):
        return _core.BoolVector_insert(self, *args)

    def reserve(self, n):
        return _core.BoolVector_reserve(self, n)

    def capacity(self):
        return _core.BoolVector_capacity(self)
    __swig_destroy__ = _core.delete_BoolVector
    __del__ = lambda self: None
BoolVector_swigregister = _core.BoolVector_swigregister
BoolVector_swigregister(BoolVector)

class ExplorationTree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ExplorationTree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ExplorationTree, name)
    __repr__ = _swig_repr
    __swig_getmethods__["createFromSnapshot"] = lambda x: _core.ExplorationTree_createFromSnapshot
    if _newclass:
        createFromSnapshot = staticmethod(_core.ExplorationTree_createFromSnapshot)

    def __init__(self, *args):
        this = _core.new_ExplorationTree(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def createSnapshot(self):
        return _core.ExplorationTree_createSnapshot(self)

    def runOperation(self, operation):
        return _core.ExplorationTree_runOperation(self, operation)

    def fetchLeaves(self):
        return _core.ExplorationTree_fetchLeaves(self)

    def fetchMol(self, canonSMILES):
        return _core.ExplorationTree_fetchMol(self, canonSMILES)

    def hasMol(self, canonSMILES):
        return _core.ExplorationTree_hasMol(self, canonSMILES)

    def deleteSubtree(self, canonSMILES):
        return _core.ExplorationTree_deleteSubtree(self, canonSMILES)

    def generateMorphs(self):
        return _core.ExplorationTree_generateMorphs(self)

    def sortMorphs(self):
        return _core.ExplorationTree_sortMorphs(self)

    def filterMorphs(self, *args):
        return _core.ExplorationTree_filterMorphs(self, *args)

    def extend(self):
        return _core.ExplorationTree_extend(self)

    def prune(self):
        return _core.ExplorationTree_prune(self)

    def getThreadCount(self):
        return _core.ExplorationTree_getThreadCount(self)

    def getGenerationCount(self):
        return _core.ExplorationTree_getGenerationCount(self)

    def getParams(self):
        return _core.ExplorationTree_getParams(self)

    def getCandidateMorphs(self):
        return _core.ExplorationTree_getCandidateMorphs(self)

    def getCandidateMorphsMask(self):
        return _core.ExplorationTree_getCandidateMorphsMask(self)

    def setThreadCount(self, threadCnt):
        return _core.ExplorationTree_setThreadCount(self, threadCnt)

    def setParams(self, params):
        return _core.ExplorationTree_setParams(self, params)

    def setCandidateMorphsMask(self, arg2):
        return _core.ExplorationTree_setCandidateMorphsMask(self, arg2)
    __swig_destroy__ = _core.delete_ExplorationTree
    __del__ = lambda self: None
ExplorationTree_swigregister = _core.ExplorationTree_swigregister
ExplorationTree_swigregister(ExplorationTree)

def ExplorationTree_createFromSnapshot(snapshot):
    return _core.ExplorationTree_createFromSnapshot(snapshot)
ExplorationTree_createFromSnapshot = _core.ExplorationTree_createFromSnapshot

# This file is compatible with both classic and new-style classes.


