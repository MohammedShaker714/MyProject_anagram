import unittest
from app import get_anagrams_dict
from app import get_anagrams

dictionary_list = ['listen', 'enlist', 'inlets', 'fried', 'silent', 'tinsel', 'silent', 'tinsel', 'fired']
anagr_dict = {
    'defir': ['fried', 'fired'],
    'eilnst': ['listen', 'enlist', 'inlets', 'silent', 'tinsel', 'silent', 'tinsel']
}


class TestAnagrams(unittest.TestCase):
    def test_anagrams_dict(self):
        self.assertEqual(get_anagrams_dict(dictionary_list), anagr_dict)

    def test_get_anagrams(self):
        self.assertEqual(get_anagrams(anagr_dict, 'fired'), "['fried']")


if __name__ == '__main__':
    unittest.main()
