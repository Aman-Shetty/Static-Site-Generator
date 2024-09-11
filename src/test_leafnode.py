import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        string = '<p>This is a paragraph of text.</p>'
        string2 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), string)
        self.assertEqual(node2.to_html(), string2)

    def test_exception(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError)

    def test_no_tag(self):
        node = LeafNode(None, "This is a raw text.")
        self.assertEqual(node.to_html(), "This is a raw text.")
