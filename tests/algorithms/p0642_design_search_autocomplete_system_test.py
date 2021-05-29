import unittest
from leetcode.algorithms.p0642_design_search_autocomplete_system \
    import AutocompleteSystem


class TestDesignSearchAutocompleteSystem(unittest.TestCase):
    def test_design_search_autocomplete_system(self):
        autocomplete_system = AutocompleteSystem(
            ['i love you', 'island', 'iroman', 'i love leetcode'],
            [5, 3, 2, 2])

        self.assertListEqual(['i love you', 'island', 'i love leetcode'],
                             autocomplete_system.input('i'))
        self.assertListEqual(['i love you', 'i love leetcode'],
                             autocomplete_system.input(' '))
        self.assertListEqual([], autocomplete_system.input('a'))
        self.assertListEqual([], autocomplete_system.input('#'))
