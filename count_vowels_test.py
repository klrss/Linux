import unittest
import count_vowels

class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        txt ="Linux administration with bash"
        result = count_vowels.get_res(txt)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()