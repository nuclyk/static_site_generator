import unittest
from htmlnode import HtmlNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(
            "a",
            "Link to somwhere",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_for_children(self):
        node = HtmlNode(
            "div",
            children=[HtmlNode()],
        )
        self.assertIsNotNone(node.children)

    def test_for_value(self):
        node = HtmlNode("p", "Some sort of text")
        self.assertIsNotNone(node.value)


if __name__ == "__main__":
    unittest.main()
