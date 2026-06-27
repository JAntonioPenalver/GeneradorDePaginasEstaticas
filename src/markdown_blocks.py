def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Split a markdown string into blocks separated by double newlines.
    Each block is stripped of leading/trailing whitespace.
    Empty blocks are removed.
    """
    # Split by double newline
    blocks = markdown.split("\n\n")
    
    # Strip whitespace from each block and filter out empty ones
    filtered_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped:  # Only add non-empty blocks
            filtered_blocks.append(stripped)
    
    return filtered_blocks
