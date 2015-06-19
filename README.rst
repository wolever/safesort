``safesort``: safely sort heterogeneous collections on Python 2 and 3
=====================================================================

.. image:: https://travis-ci.org/wolever/safesort.svg?branch=master
    :target: https://travis-ci.org/wolever/safesort


``safesort`` does what it says on the box: guarantees safe sorting of arbitrary
heterogeneous lists across Python 2 and Python 3::

    >>> list(sorted(["a", 1, None]))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: int() < str()
    >>> list(safesort(["a", 1, None))
    [None, 1, 'a']

Three ordering keys are attempted for each comparison:

    1. Object: ``objA > objB``

    2. Type-and-object: ``(type(objA).__mro__, objA) > (type(objB).__mro__, objB)``

    3. Type-and-identity: ``(type(objA).__mro__, id(objA)) > (type(objB).__mro__, id(objB))``

This guarantees a total ordering which is:

    1. As consistent as possible
    2. Broadly sensible: objects with similar types will be grouped together

For example::

    >>> from safesort import safesort
    >>> input = ['a', set([]), [], {}, 1, None]
    >>> list(safesort(input))
    [None, 1, {}, [], set([]), 'a']


Installation
------------

``safesort`` can be installed with Python 2 or Python 3 using ``pip`` or
``easy_install``::

    $ pip install safesort
    - OR -
    $ easy_install safesort
