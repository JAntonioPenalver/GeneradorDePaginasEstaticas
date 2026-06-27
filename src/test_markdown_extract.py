import unittest
from markdown_extract import extract_markdown_images, extract_markdown_links

class TestMarkdownExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
            matches
        )
    
    def test_extract_markdown_images_no_images(self):
        text = "This is text without any images"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
    
    def test_extract_markdown_links_multiple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )
    
    def test_extract_markdown_links_no_links(self):
        text = "This is text without any links"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links_and_images(self):
        # Make sure image extraction doesn't pick up links and vice versa
        text = "Image ![alt](url) and link [text](url)"
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertListEqual([("alt", "url")], images)
        self.assertListEqual([("text", "url")], links)
    
    def test_extract_markdown_images_with_complex_url(self):
        text = "Image ![diagram](https://example.com/path/to/image.png?v=1&format=png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("diagram", "https://example.com/path/to/image.png?v=1&format=png")], matches)
    
    def test_extract_markdown_links_with_complex_url(self):
        text = "Link [search](https://example.com/search?q=test&lang=en)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("search", "https://example.com/search?q=test&lang=en")], matches)

if __name__ == "__main__":
    unittest.main()
