import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph", None, {"href":"src/"})
        node2 = HTMLNode("p", "this is a paragraph", None, {"href":"src/"})
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_error(self):
        node = HTMLNode("p", "this is a paragraph", None, {"href":"src/"})
        self.assertRaises(NotImplementedError)

    def test_props_to_html(self):
        node = HTMLNode(props={
            "href" : "https://www.google.com",
            "target": "_blank",
        })

        string = node.props_to_html()
        self.assertEqual(string, ' href="https://www.google.com" target="_blank"')
