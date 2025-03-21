from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("Value are required")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        elif self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
