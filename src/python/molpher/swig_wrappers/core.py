# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
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
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
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
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _core.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _core.SwigPyIterator_value(self)
    def incr(self, n=1): return _core.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _core.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _core.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _core.SwigPyIterator_equal(self, *args)
    def copy(self): return _core.SwigPyIterator_copy(self)
    def next(self): return _core.SwigPyIterator_next(self)
    def __next__(self): return _core.SwigPyIterator___next__(self)
    def previous(self): return _core.SwigPyIterator_previous(self)
    def advance(self, *args): return _core.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _core.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _core.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _core.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _core.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _core.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _core.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _core.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


def load_data_from(*args):
  return _core.load_data_from(*args)
load_data_from = _core.load_data_from
SHARED_PTR_DISOWN = _core.SHARED_PTR_DISOWN
class MolVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MolVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MolVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _core.MolVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _core.MolVector___nonzero__(self)
    def __bool__(self): return _core.MolVector___bool__(self)
    def __len__(self): return _core.MolVector___len__(self)
    def pop(self): return _core.MolVector_pop(self)
    def __getslice__(self, *args): return _core.MolVector___getslice__(self, *args)
    def __setslice__(self, *args): return _core.MolVector___setslice__(self, *args)
    def __delslice__(self, *args): return _core.MolVector___delslice__(self, *args)
    def __delitem__(self, *args): return _core.MolVector___delitem__(self, *args)
    def __getitem__(self, *args): return _core.MolVector___getitem__(self, *args)
    def __setitem__(self, *args): return _core.MolVector___setitem__(self, *args)
    def append(self, *args): return _core.MolVector_append(self, *args)
    def empty(self): return _core.MolVector_empty(self)
    def size(self): return _core.MolVector_size(self)
    def clear(self): return _core.MolVector_clear(self)
    def swap(self, *args): return _core.MolVector_swap(self, *args)
    def get_allocator(self): return _core.MolVector_get_allocator(self)
    def begin(self): return _core.MolVector_begin(self)
    def end(self): return _core.MolVector_end(self)
    def rbegin(self): return _core.MolVector_rbegin(self)
    def rend(self): return _core.MolVector_rend(self)
    def pop_back(self): return _core.MolVector_pop_back(self)
    def erase(self, *args): return _core.MolVector_erase(self, *args)
    def __init__(self, *args): 
        this = _core.new_MolVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _core.MolVector_push_back(self, *args)
    def front(self): return _core.MolVector_front(self)
    def back(self): return _core.MolVector_back(self)
    def assign(self, *args): return _core.MolVector_assign(self, *args)
    def resize(self, *args): return _core.MolVector_resize(self, *args)
    def insert(self, *args): return _core.MolVector_insert(self, *args)
    def reserve(self, *args): return _core.MolVector_reserve(self, *args)
    def capacity(self): return _core.MolVector_capacity(self)
    __swig_destroy__ = _core.delete_MolVector
    __del__ = lambda self : None;
MolVector_swigregister = _core.MolVector_swigregister
MolVector_swigregister(MolVector)

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
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _core.delete_TreeOperation
    __del__ = lambda self : None;
    def __call__(self): return _core.TreeOperation___call__(self)
    def getTree(self): return _core.TreeOperation_getTree(self)
    def setTree(self, *args): return _core.TreeOperation_setTree(self, *args)
    def __disown__(self):
        self.this.disown()
        _core.disown_TreeOperation(self)
        return weakref_proxy(self)
TreeOperation_swigregister = _core.TreeOperation_swigregister
TreeOperation_swigregister(TreeOperation)

class FindLeavesOper(TreeOperation):
    __swig_setmethods__ = {}
    for _s in [TreeOperation]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FindLeavesOper, name, value)
    __swig_getmethods__ = {}
    for _s in [TreeOperation]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, FindLeavesOper, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _core.new_FindLeavesOper(*args)
        try: self.this.append(this)
        except: self.this = this
    def __call__(self): return _core.FindLeavesOper___call__(self)
    def fetchLeaves(self): return _core.FindLeavesOper_fetchLeaves(self)
    __swig_destroy__ = _core.delete_FindLeavesOper
    __del__ = lambda self : None;
FindLeavesOper_swigregister = _core.FindLeavesOper_swigregister
FindLeavesOper_swigregister(FindLeavesOper)

class StringSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringSet, name)
    __repr__ = _swig_repr
    def iterator(self): return _core.StringSet_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _core.StringSet___nonzero__(self)
    def __bool__(self): return _core.StringSet___bool__(self)
    def __len__(self): return _core.StringSet___len__(self)
    def append(self, *args): return _core.StringSet_append(self, *args)
    def __contains__(self, *args): return _core.StringSet___contains__(self, *args)
    def __getitem__(self, *args): return _core.StringSet___getitem__(self, *args)
    def add(self, *args): return _core.StringSet_add(self, *args)
    def discard(self, *args): return _core.StringSet_discard(self, *args)
    def __init__(self, *args): 
        this = _core.new_StringSet(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _core.StringSet_empty(self)
    def size(self): return _core.StringSet_size(self)
    def clear(self): return _core.StringSet_clear(self)
    def swap(self, *args): return _core.StringSet_swap(self, *args)
    def count(self, *args): return _core.StringSet_count(self, *args)
    def begin(self): return _core.StringSet_begin(self)
    def end(self): return _core.StringSet_end(self)
    def rbegin(self): return _core.StringSet_rbegin(self)
    def rend(self): return _core.StringSet_rend(self)
    def erase(self, *args): return _core.StringSet_erase(self, *args)
    def find(self, *args): return _core.StringSet_find(self, *args)
    def lower_bound(self, *args): return _core.StringSet_lower_bound(self, *args)
    def upper_bound(self, *args): return _core.StringSet_upper_bound(self, *args)
    def equal_range(self, *args): return _core.StringSet_equal_range(self, *args)
    def insert(self, *args): return _core.StringSet_insert(self, *args)
    __swig_destroy__ = _core.delete_StringSet
    __del__ = lambda self : None;
StringSet_swigregister = _core.StringSet_swigregister
StringSet_swigregister(StringSet)

class MolpherMol(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MolpherMol, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MolpherMol, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _core.new_MolpherMol(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _core.delete_MolpherMol
    __del__ = lambda self : None;
    def copy(self): return _core.MolpherMol_copy(self)
    def getSMILES(self): return _core.MolpherMol_getSMILES(self)
    def getDistToTarget(self): return _core.MolpherMol_getDistToTarget(self)
    def getTree(self): return _core.MolpherMol_getTree(self)
    def getParentSMILES(self): return _core.MolpherMol_getParentSMILES(self)
    def getDescendants(self): return _core.MolpherMol_getDescendants(self)
    def getHistoricDescendants(self): return _core.MolpherMol_getHistoricDescendants(self)
    def getItersWithoutDistImprovement(self): return _core.MolpherMol_getItersWithoutDistImprovement(self)
    def getSAScore(self): return _core.MolpherMol_getSAScore(self)
    def getMolecularWeight(self): return _core.MolpherMol_getMolecularWeight(self)
    def getFormula(self): return _core.MolpherMol_getFormula(self)
    def getParentOper(self): return _core.MolpherMol_getParentOper(self)
    def setOwner(self, *args): return _core.MolpherMol_setOwner(self, *args)
    def setSMILES(self, *args): return _core.MolpherMol_setSMILES(self, *args)
    def setParentSMILES(self, *args): return _core.MolpherMol_setParentSMILES(self, *args)
    def setDistToTarget(self, *args): return _core.MolpherMol_setDistToTarget(self, *args)
    def setSAScore(self, *args): return _core.MolpherMol_setSAScore(self, *args)
    def setItersWithoutDistImprovement(self, *args): return _core.MolpherMol_setItersWithoutDistImprovement(self, *args)
    def increaseItersWithoutDistImprovement(self): return _core.MolpherMol_increaseItersWithoutDistImprovement(self)
    def decreaseItersWithoutDistImprovement(self): return _core.MolpherMol_decreaseItersWithoutDistImprovement(self)
    def addToDescendants(self, *args): return _core.MolpherMol_addToDescendants(self, *args)
    def removeFromDescendants(self, *args): return _core.MolpherMol_removeFromDescendants(self, *args)
    def setDescendants(self, *args): return _core.MolpherMol_setDescendants(self, *args)
    def addToHistoricDescendants(self, *args): return _core.MolpherMol_addToHistoricDescendants(self, *args)
    def removeFromHistoricDescendants(self, *args): return _core.MolpherMol_removeFromHistoricDescendants(self, *args)
    def setHistoricDescendants(self, *args): return _core.MolpherMol_setHistoricDescendants(self, *args)
    def isValid(self): return _core.MolpherMol_isValid(self)
    def isBoundToTree(self): return _core.MolpherMol_isBoundToTree(self)
MolpherMol_swigregister = _core.MolpherMol_swigregister
MolpherMol_swigregister(MolpherMol)

# This file is compatible with both classic and new-style classes.


