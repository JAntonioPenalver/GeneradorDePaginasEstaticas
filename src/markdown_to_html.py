from markdown_blocks import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from split_nodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

def text_to_children(text: str) -> list:
    """
    Convert text with inline markdown to a list of HTMLNode children.
    """
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def block_to_html_node(block: str) -> HTMLNode:
    """
    Convert a single markdown block to an HTMLNode.
    """
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    else:
        raise ValueError(f"Unknown block type: {block_type}")

def heading_to_html_node(block: str) -> HTMLNode:
    """
    Convert a heading block to an HTMLNode.
    Extract the level and text, then create the appropriate tag.
    """
    lines = block.split("\n")
    first_line = lines[0]
    
    # Count the # characters
    level = 0
    for char in first_line:
        if char == "#":
            level += 1
        else:
            break
    
    # Extract text after the # characters and space
    text = first_line[level + 1:]
    
    # Create children from inline markdown
    children = text_to_children(text)
    
    # Create the heading tag
    tag = f"h{level}"
    return ParentNode(tag, children)

def paragraph_to_html_node(block: str) -> HTMLNode:
    """
    Convert a paragraph block to an HTMLNode.
    Join all lines and parse inline markdown.
    """
    # Join lines with spaces (remove newlines)
    text = " ".join(block.split("\n"))
    
    # Create children from inline markdown
    children = text_to_children(text)
    
    return ParentNode("p", children)

def code_to_html_node(block: str) -> HTMLNode:
    lines = block.split(chr(10))
    if len(lines) >= 2:
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
    text = chr(10).join(lines) + chr(10)
    code_node = LeafNode("code", text)
    return ParentNode("pre", [code_node])
def quote_to_html_node(block: str) -> HTMLNode:
    """
    Convert a quote block to an HTMLNode.
    Remove the > from each line and parse inline markdown.
    """
    lines = block.split("\n")
    
    # Remove > from each line
    quote_lines = []
    for line in lines:
        if line.startswith(">"):
            # Remove > and optional space
            if line.startswith("> "):
                quote_lines.append(line[2:])
            else:
                quote_lines.append(line[1:])
        else:
            quote_lines.append(line)
    
    # Join lines and create children
    text = " ".join(quote_lines)
    children = text_to_children(text)
    
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block: str) -> HTMLNode:
    """
    Convert an unordered list block to an HTMLNode.
    Create li items for each line.
    """
    lines = block.split("\n")
    
    li_children = []
    for line in lines:
        # Remove the - or * and space
        if line.startswith("- "):
            text = line[2:]
        elif line.startswith("* "):
            text = line[2:]
        else:
            text = line
        
        # Create children from inline markdown
        children = text_to_children(text)
        
        # Create li node
        li_node = ParentNode("li", children)
        li_children.append(li_node)
    
    # Create ul node
    return ParentNode("ul", li_children)

def ordered_list_to_html_node(block: str) -> HTMLNode:
    """
    Convert an ordered list block to an HTMLNode.
    Create li items for each line.
    """
    lines = block.split("\n")
    
    li_children = []
    for line in lines:
        # Remove the number. and space
        # Find the first space after the number
        dot_index = line.find(".")
        text = line[dot_index + 2:]
        
        # Create children from inline markdown
        children = text_to_children(text)
        
        # Create li node
        li_node = ParentNode("li", children)
        li_children.append(li_node)
    
    # Create ol node
    return ParentNode("ol", li_children)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    Convert a full markdown document to an HTMLNode.
    """
    # Split into blocks
    blocks = markdown_to_blocks(markdown)
    
    # Convert each block to an HTMLNode
    block_nodes = []
    for block in blocks:
        block_node = block_to_html_node(block)
        block_nodes.append(block_node)
    
    # Create a parent div containing all blocks
    return ParentNode("div", block_nodes)
