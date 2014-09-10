**WARNING** THIS EXISTS ONLY AS AN RFC; NOT READY FOR ANY SORT OF REAL-WORLD USE **WARNING**

``safesort``: safely sort heterogeneous collections on Python 2 and 3
=====================================================================

.. image:: https://travis-ci.org/wolever/safesort.svg?branch=master
    :target: https://travis-ci.org/wolever/safesort


``safesort`` does what it says on the box: guarantees safe sorting of arbitrary
heterogeneous lists across Python 2 and Python 3.

Three ordering keys are attempted for each comparison:

1. Object-to-object: ``objA > objB``

2. Type-and-object: ``(type(objA).__mro__, objA) > (type(objB).__mro__, objB)``

3. Type-and-identity: ``(type(objA).__mro__, id(objA)) > (type(objB).__mro__, id(objB))``

This guarantees a total ordering which is:

1. As consistent as possible

2. Broadly sensible: objects with similar types will be grouped together

For example::

    >>> from safesort import safesort
    >>> input = [None, 1, {}, [], set([]), 'a']
    >>> input.reverse()
    >>> list(safesort(input))
    [None, 1, {}, [], set([]), 'a']

Note: ``SafelySortable`` class implements a ``__hash__`` method which will
guarantees that ``hash(SafelySortable(x)) == hash(SafelySortable(y))`` if
``SafelySortable(x) == SafelySortable(y)`` for all reasonable implementations
of ``x`` and ``y``. The implementation is *blindingly* naive, though::

    def __hash__(self):
        try:
            return hash(self.obj)
        except TypeError:
            pass
        return 1

And really *should not be used* unless absolutely necessary.

TODO: is implementing __hash__ even a good idea? Maybe it should just TypeError
out all the time?


.. comment::

    Installation
    ------------

    ``safesort`` can be installed with Python 2 or Python 3 using ``pip`` or
    ``easy_install``::

        $ pip install safesort
        - OR -
        $ easy_install safesort
