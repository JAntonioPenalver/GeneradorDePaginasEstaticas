import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_codeblock(self):
        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_heading(self):
        md = "# This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1></div>")
    
    def test_heading_with_inline_markdown(self):
        md = "## This is a **bold** heading with _italic_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is a <b>bold</b> heading with <i>italic</i></h2></div>",
        )
    
    def test_quote(self):
        md = "> This is a quote\n> on multiple lines\n> with content"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote on multiple lines with content</blockquote></div>",
        )
    
    def test_quote_with_inline_markdown(self):
        md = "> This is a **bold** quote with _italic_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a <b>bold</b> quote with <i>italic</i></blockquote></div>",
        )
    
    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )
    
    def test_unordered_list_with_inline_markdown(self):
        md = "- **Bold** item\n- _Italic_ item\n- `Code` item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li><b>Bold</b> item</li><li><i>Italic</i> item</li><li><code>Code</code> item</li></ul></div>",
        )
    
    def test_ordered_list(self):
        md = "1. First item\n2. Second item\n3. Third item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )
    
    def test_ordered_list_with_inline_markdown(self):
        md = "1. **Bold** first\n2. _Italic_ second\n3. `Code` third"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li><b>Bold</b> first</li><li><i>Italic</i> second</li><li><code>Code</code> third</li></ol></div>",
        )
    
    def test_mixed_blocks(self):
        md = "# Heading\n\nThis is a paragraph\n\n- List item 1\n- List item 2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<h1>Heading</h1>", html)
        self.assertIn("<p>This is a paragraph</p>", html)
        self.assertIn("<ul>", html)
        self.assertIn("<li>List item 1</li>", html)
    
    def test_paragraph_with_link(self):
        md = "This is a paragraph with a [link](https://boot.dev)"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is a paragraph with a <a href="https://boot.dev">link</a></p></div>',
        )
    
    def test_paragraph_with_image(self):
        md = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn('<img src="https://i.imgur.com/zjjcJKZ.png" alt="image"', html)

if __name__ == "__main__":
    unittest.main()
