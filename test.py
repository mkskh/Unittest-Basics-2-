from text import to_upper, to_word_list_isupper
import unittest

class TestText(unittest.TestCase):

    # TASK 1
    def test_check_upper(self):
        result = to_upper('abcdef')
        self.assertEqual(result, "ABCDEF")

    # TASK 2
    def test_list_upper(self):
        result = to_word_list_isupper(['I', 'LOVE', 'YOU'])
        self.assertTrue(result == True)

    # TASK 3
    def test_list_not_upper(self):
        result = to_word_list_isupper(['i', 'LOVE', 'YOU'])
        self.assertFalse(result == True)

    # TASK 4 
    def test_raises_error_input_type_upper(self):
        with self.assertRaises(TypeError):
            to_upper(543)
    
    # TASK 5
    def test_raises_error_list_isupper(self):
        with self.assertRaises(TypeError): 
            to_word_list_isupper('string')

if __name__ == '__main__':
    unittest.main()