class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Method not Implemented")

    def props_to_html(self) -> str:
        string = ''
        if self.props is None:
            return string
        for value in self.props.keys():
            string += f' {value}="{self.props[value]}"'
        return string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value = str(None), props=None):
        super().__init__(tag = tag, value = value, children= None, props = props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode has no value given.")
        elif self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children = list(), props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("HTML tag value not provided.")
        elif self.children == None:
            raise ValueError("HTML tag has no child node given.")
        else:
            string = ""
            for node in self.children:
                string += node.to_html()
            st = f"<{self.tag}{self.props_to_html()}>{string}</{self.tag}>"
            return st

    def __repr__(self) -> str:
            return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
