from markdown_to_html import markdown_to_html_node
from textnode import TextNode
import os
import shutil


def extract_title(markdown):
    lines = markdown.split("\n")
    header = lines[0]
    if header.startswith("# "):
        return header.lstrip("#").strip()
    raise ValueError("invalid header")


def copy_files(src, dst):
    if os.path.isfile(src):
        shutil.copy(src, dst)
        return src
    else:
        if not os.path.exists(dst):
            os.mkdir(dst)

    for path in os.listdir(src):
        copy_files(os.path.join(src, path), os.path.join(dst, path))


def generate_page(from_path, template_path, dest_path):
    markdown = None
    template = None
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()
        file.close()
    with open(template_path, "r") as file:
        template = file.read()
        file.close()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    # create dir if it doesn't exist
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as file:
        file.write(template)
        file.close()


def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    generate_page("./content/index.md", "./template.html", "./static/index.html")
    copy_files("./static", "./public")


if __name__ == "__main__":
    main()
