import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#   Tolkien Fan Club  "), "Tolkien Fan Club")
        self.assertEqual(extract_title("# Line 1\n## Line 2"), "Line 1")

    def test_extract_title_missing(self):
        with self.assertRaises(Exception):
            extract_title("## Only an H2 here")
        with self.assertRaises(Exception):
            extract_title("Just text")

if __name__ == "__main__":
    unittest.main()
