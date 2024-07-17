import unittest
from text import to_upper, to_word_list_isupper

class TestStringMethods(unittest.TestCase):
    # Task1
    def test_upper1(self):
        self.assertEqual(to_upper('abcdef'), 'ABCDEF', 'to_upper function does not return expected value')
    # Task2    
    def test_word_list_isupper1(self):
        self.assertTrue(to_word_list_isupper(['I', 'LOVE', 'PYTHON' ]), 'to_word_list_isupper should return True')
    # Task3    
    def test_word_list_isupper2(self):
        self.assertFalse(to_word_list_isupper(['i', 'LOVE', 'PYTHON' ]), 'to_word_list_isupper should return False')
    # Task4
    def test_upper3(self):
        with self.assertRaises(TypeError):
            to_upper(523)
    # Task5
    def test_word_list_isupper3(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper("I LOVE YOU")


