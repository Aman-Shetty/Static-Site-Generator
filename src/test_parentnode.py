import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
        self.assertEqual(
                    node.to_html(),
                    "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
                )

    def test_no_tag(self):
        node1 = ParentNode(
            None,
            children= [
                LeafNode("b", "Bold text"),
            ],
        )
        self.assertRaises(ValueError)

    def test_no_children(self):
        node2 = ParentNode(
            "p",
            None,
        )
        self.assertRaises(ValueError)
