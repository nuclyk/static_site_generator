from gencontent import copy_files, generate_pages_recursive
from markdown_to_html import markdown_to_html_node
from textnode import TextNode
import os
import shutil
import pathlib


def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    copy_files("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./static")


if __name__ == "__main__":
    main()
