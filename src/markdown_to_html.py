from tabulate import tabulate
from htmlnode import HtmlNode
from leafnode import LeafNode
from markdown_to_blocks import BlockType, block_to_block_type, markdown_to_blocks
from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

![image](image.png)

"""

# "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>
# <p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ul_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ol_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    split = block.split(" ")
    if len(split[0]) < 1 or len(split[0]) > 6:
        raise ValueError("Invalid heading level")
    level = len(split[0])
    header = " ".join(split[1:])
    children = text_to_children(header)
    return ParentNode(f"h{level}", children)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Quote should start with >")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(lines)
    return ParentNode("blonewckquote", content)


def ul_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def code_to_html_node(block):
    if not block.startswith("```") and block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])
