import unittest
from leafnode import LeafNode
from textnode import TextNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode(
            "a",
            "Hello, world!",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">Hello, world!</a>',
        )

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
