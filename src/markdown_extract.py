import re

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """
    Extract markdown images from text.
    Returns list of tuples: (alt_text, url)
    Pattern: ![alt text](url)
    """
    pattern = r"!\[([^\]]*)\]\(([^\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """
    Extract markdown links from text.
    Returns list of tuples: (link_text, url)
    Pattern: [link text](url) pero NOT ![...](...)
    """
    pattern = r"(?<!\!)\[([^\]]*)\]\(([^\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
