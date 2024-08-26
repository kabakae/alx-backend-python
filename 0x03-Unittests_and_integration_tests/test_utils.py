#!/usr/bin/env python3
"""
test_utils.py

Unit tests for the access_nested_map function in the utils module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: dict, path: tuple, expected: object
    ) -> None:
        """
        Test that access_nested_map returns the expected value
        for given nested_map and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(
        self, nested_map: dict, path: tuple, expected: str
    ) -> None:
        """
        Test that access_nested_map raises a KeyError with the expected message
        for invalid paths in the nested_map.
        """
        with self.assertRaisesRegex(KeyError, expected):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
