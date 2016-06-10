# coding=utf-8
import unittest
from interview_questions import arrays_and_strings


class TestInterviewQuestions(unittest.TestCase):
    def test_true_unique_letters_in_ascii_string(self):
        result = arrays_and_strings.unique_letters_in_ascii_string("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(result, True)

    def test_false_unique_letters_in_ascii_string(self):
        result = arrays_and_strings.unique_letters_in_ascii_string("abcdefghijjklmnopqrstuvwxyz")
        self.assertEqual(result, False)
