import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_single_block(self):
        md = "This is a single block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single block"])
    
    def test_markdown_to_blocks_multiple_blocks(self):
        md = "Block 1\n\nBlock 2\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])
    
    def test_markdown_to_blocks_with_leading_trailing_whitespace(self):
        md = """
   Block 1   

   Block 2   
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2"])
    
    def test_markdown_to_blocks_with_excessive_newlines(self):
        md = "Block 1\n\n\n\nBlock 2\n\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])
    
    def test_markdown_to_blocks_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_markdown_to_blocks_only_whitespace(self):
        md = "   \n\n   \n\n   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_markdown_to_blocks_heading_paragraph_list(self):
        md = """# Heading

This is a paragraph

- List item 1
- List item 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "This is a paragraph",
                "- List item 1\n- List item 2",
            ],
        )
    
    def test_markdown_to_blocks_multiline_paragraph(self):
        md = """This is line 1
This is line 2
This is line 3

This is a new block"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is line 1\nThis is line 2\nThis is line 3",
                "This is a new block",
            ],
        )

if __name__ == "__main__":
    unittest.main()
