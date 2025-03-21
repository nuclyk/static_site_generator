from textnode import TextNode
import os
import shutil

# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree


def copy(src, dst):
    if os.path.isfile(src):
        shutil.copy(src, dst)
        return src
    else:
        if not os.path.exists(dst):
            os.mkdir(dst)

    for path in os.listdir(src):
        copy(os.path.join(src, path), os.path.join(dst, path))


def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    copy("./static", "./public")


if __name__ == "__main__":
    main()
