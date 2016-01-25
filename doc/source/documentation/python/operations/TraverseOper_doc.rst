TraverseOper
============

.. py:currentmodule:: molpher.swig_wrappers.core

.. autoclass:: TraverseOper
    :show-inheritance:

    :param \*args: the `exploration tree` and the callback to call. Optionally we can specify
        a `morph` which will define the root of the subtree to traverse. If no root
        is specified, then the `source molecule` is selected automatically.
    :type \*args: `ExplorationTree`, `TraverseCallback` and `MolpherMol` (optional)

    A `tree operation` that can register a `TraverseCallback` and call its
    :py:meth:`~TraverseCallback.processMorph` method on every molecule it encounters in the given subtree
    (defined by its root).

    .. automethod:: __call__

        Run the attached callback on every molecule in the subtree with the given root.
