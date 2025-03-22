import sys
from gencontent import copy_files, generate_pages_recursive
from markdown_to_html import markdown_to_html_node
from textnode import TextNode
import os
import shutil

BASEPATH = "/"

dir_path_public = "./public"
dir_path_docs = "./docs"
dir_path_static = "./static"
dir_path_content = "./content"
path_template = "./template.html"


def main():
    global BASEPATH
    if len(sys.argv) == 2:
        BASEPATH = sys.argv[1]

    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    copy_files(dir_path_static, dir_path_docs)
    generate_pages_recursive(dir_path_content, path_template, dir_path_static, BASEPATH)


if __name__ == "__main__":
    main()
