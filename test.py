from __future__ import print_function

import unittest

from safesort import safesort

class TotallyUnSortable(object):
    def _type_error(self, *a):
        raise TypeError()
    __nonzero__ = _type_error
    __bool__ = _type_error
    __cmp__ = _type_error
    __lt__ = _type_error
    __gt__ = _type_error
    __eq__ = _type_error
    __hash__ = _type_error


class SafesortTests(unittest.TestCase):
    def assertSortable(self, input):
        list(safesort(reversed(input)))

    def test_safesort_py27_consistant_ordering(self):
        self.assertSortable([None, 1, {}, [], set([]), 'a'])

    def test_totally_unsortable(self):
        self.assertSortable([TotallyUnSortable(), set(), 3])


if __name__ == "__main__":
    unittest.main()
