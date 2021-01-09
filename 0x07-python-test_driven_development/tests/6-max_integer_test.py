#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest class for testing max_integer"""

    def test_max(self):
        """tests that function returns the correct output for valid input"""

        self.assertEqual(max_integer([-5, 0, 30, 7, 12, -1]), 30)
        self.assertEqual(max_integer([-5, 0, -30, -7, -12, -1]), 0)
        self.assertEqual(max_integer([-5, -10, -30, -7, -12, -1]), -1)
        self.assertEqual(max_integer([8]), 8)
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        """tests that max_integer is recieveing a list of ints"""

        self.assertRaises(TypeError, max_integer(), ["cat", "in", "the", "hat"])
        self.assertRaises(TypeError, max_integer(), [6.9, 4.0, 2.8, 3.4])
        self.assertRaises(TypeError, max_integer(), [[1, 2, 3], [4, 5, 6]])
        self.assertRaises(TypeError, max_integer(), (2, 8, 16))
        self.assertRaises(TypeError, max_integer(), (2j, 8j, 16j))
        self.assertRaises(TypeError, max_integer(), 16)
