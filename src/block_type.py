from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    """
    Determine the type of a markdown block.
    """
    lines = block.split("\n")
    
    # Check for heading (1-6 # followed by space)
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    # Check for code block (starts and ends with 3 backticks)
    # Remove empty lines at end for checking
    non_empty_lines = [line for line in lines if line.strip()]
    if len(non_empty_lines) >= 2:
        first_line = non_empty_lines[0].strip()
        last_line = non_empty_lines[-1].strip()
        if first_line.startswith("```") and last_line == "```":
            return BlockType.CODE
    
    # Check for quote (every line starts with >)
    if lines and all(line.startswith(">") for line in lines if line.strip()):
        # Make sure there's at least one non-empty line
        if any(line.strip() for line in lines):
            return BlockType.QUOTE
    
    # Check for unordered list (every line starts with - or * followed by space)
    if lines and all(line.startswith("- ") or line.startswith("* ") for line in lines if line.strip()):
        # Make sure there's at least one non-empty line
        if any(line.strip() for line in lines):
            return BlockType.UNORDERED_LIST
    
    # Check for ordered list (each line starts with number. space, incrementing from 1)
    is_ordered_list = True
    non_empty_idx = 0
    for line in lines:
        if not line.strip():
            continue
        expected_num = non_empty_idx + 1
        if not re.match(rf"^{expected_num}\. ", line):
            is_ordered_list = False
            break
        non_empty_idx += 1
    
    if is_ordered_list and non_empty_idx > 0:
        return BlockType.ORDERED_LIST
    
    # Default to paragraph
    return BlockType.PARAGRAPH
