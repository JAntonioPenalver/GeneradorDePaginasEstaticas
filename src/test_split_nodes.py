import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
    
    def test_split_bold(self):
        node = TextNode("This is text with **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )
    
    def test_split_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ]
        )
    
    def test_split_multiple_delimiters(self):
        node = TextNode("This has `code` and `more code` blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("more code", TextType.CODE),
                TextNode(" blocks", TextType.TEXT),
            ]
        )
    
    def test_split_non_text_node(self):
        # Non-TEXT nodes should pass through unchanged
        bold_node = TextNode("bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([bold_node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [bold_node])
    
    def test_split_mixed_nodes(self):
        # Mix of TEXT and non-TEXT nodes
        text_node = TextNode("text with `code`", TextType.TEXT)
        bold_node = TextNode("bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([text_node, bold_node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("text with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                bold_node,
            ]
        )
    
    def test_unclosed_delimiter_raises(self):
        node = TextNode("This has `unclosed code", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
    
    def test_delimiter_at_start(self):
        node = TextNode("`code` at start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("code", TextType.CODE),
                TextNode(" at start", TextType.TEXT),
            ]
        )
    
    def test_delimiter_at_end(self):
        node = TextNode("at end `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("at end ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ]
        )

if __name__ == "__main__":
    unittest.main()
