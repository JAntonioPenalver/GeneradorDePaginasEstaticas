import unittest
from textnode import TextNode, TextType
from split_nodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes_basic(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
    
    def test_text_to_textnodes_plain_text(self):
        text = "Just plain text"
        nodes = text_to_textnodes(text)
        self.assertListEqual([TextNode("Just plain text", TextType.TEXT)], nodes)
    
    def test_text_to_textnodes_bold_only(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            nodes
        )
    
    def test_text_to_textnodes_italic_only(self):
        text = "This is _italic_ text"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            nodes
        )
    
    def test_text_to_textnodes_code_only(self):
        text = "This is `code` text"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
            nodes
        )
    
    def test_text_to_textnodes_image_only(self):
        text = "![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            nodes
        )
    
    def test_text_to_textnodes_link_only(self):
        text = "[link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
    
    def test_text_to_textnodes_multiple_bold(self):
        text = "This is **bold one** and **bold two**"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold one", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold two", TextType.BOLD),
            ],
            nodes
        )
    
    def test_text_to_textnodes_multiple_images_and_links(self):
        text = "![img1](url1) and [link1](url1) and ![img2](url2) and [link2](url2)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "url2"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "url2"),
            ],
            nodes
        )
    
    def test_text_to_textnodes_code_with_special_chars(self):
        text = "Use `print()` function"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Use ", TextType.TEXT),
                TextNode("print()", TextType.CODE),
                TextNode(" function", TextType.TEXT),
            ],
            nodes
        )
    
    def test_text_to_textnodes_bold_italic_code(self):
        text = "**bold** _italic_ `code`"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            nodes
        )

if __name__ == "__main__":
    unittest.main()
