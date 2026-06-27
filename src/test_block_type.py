import unittest
from block_type import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_heading_h1(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_heading_h6(self):
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_heading_invalid_no_space(self):
        block = "#This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_heading_invalid_too_many_hashes(self):
        block = "####### Too many hashes"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_code_block(self):
        block = """```python
def hello():
    print("world")
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_code_block_no_language(self):
        block = """```
code here
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_code_block_invalid_missing_closing(self):
        block = """```
code here"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_quote_single_line(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_quote_multiple_lines(self):
        block = """> This is a quote
> on multiple lines
> with more content"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_quote_with_no_space_after_gt(self):
        block = """>This is a quote
>without space"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_quote_invalid_missing_gt_on_line(self):
        block = """> This is a quote
This line is missing >"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_unordered_list_dash(self):
        block = """- Item 1
- Item 2
- Item 3"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_unordered_list_asterisk(self):
        block = """* Item 1
* Item 2
* Item 3"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_unordered_list_mixed_invalid(self):
        block = """- Item 1
* Item 2
- Item 3"""
        # This should still be valid as long as each line starts with - or *
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_unordered_list_invalid_no_space(self):
        block = """- Item 1
-Item 2"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list(self):
        block = """1. First
2. Second
3. Third"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_ordered_list_single_item(self):
        block = "1. Only item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_ordered_list_invalid_wrong_start(self):
        block = """2. First
3. Second
4. Third"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list_invalid_skip_number(self):
        block = """1. First
3. Third"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list_invalid_no_space_after_dot(self):
        block = """1.First
2.Second"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_paragraph(self):
        block = "This is just a regular paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_paragraph_multiple_lines(self):
        block = """This is a paragraph
spanning multiple lines
without any special formatting"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
