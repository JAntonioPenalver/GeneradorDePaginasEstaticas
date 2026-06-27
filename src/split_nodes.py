from textnode import TextNode, TextType
from markdown_extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        # Only split TEXT type nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # Split by delimiter
        parts = node.text.split(delimiter)
        
        # If even number of parts, we have unclosed delimiters
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid markdown syntax: unclosed delimiter '{delimiter}'")
        
        # Build new nodes
        for i, part in enumerate(parts):
            if part == "":  # Skip empty strings
                continue
            
            # Odd indices are the delimited content
            if i % 2 == 1:
                new_nodes.append(TextNode(part, text_type))
            else:
                # Even indices are regular text
                new_nodes.append(TextNode(part, TextType.TEXT))
    
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        # Only split TEXT type nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # Extract all images from the text
        images = extract_markdown_images(node.text)
        
        # If no images, just add the node as-is
        if not images:
            new_nodes.append(node)
            continue
        
        # Process the text and split by images
        text = node.text
        for alt_text, url in images:
            # Find the markdown image syntax
            image_md = f"![{alt_text}]({url})"
            parts = text.split(image_md, 1)
            
            # Add the text before the image
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Continue with the remaining text
            text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        # Only split TEXT type nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # Extract all links from the text
        links = extract_markdown_links(node.text)
        
        # If no links, just add the node as-is
        if not links:
            new_nodes.append(node)
            continue
        
        # Process the text and split by links
        text = node.text
        for link_text, url in links:
            # Find the markdown link syntax
            link_md = f"[{link_text}]({url})"
            parts = text.split(link_md, 1)
            
            # Add the text before the link
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            
            # Continue with the remaining text
            text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    """
    Convert raw markdown text into a list of TextNode objects.
    Handles: bold (**), italic (_), code (`), images ![]()), and links []()
    """
    # Start with a single TEXT node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Apply splits in order
    # Order matters! Code must come before bold/italic to avoid conflicts
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes
