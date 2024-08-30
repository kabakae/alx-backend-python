#!/usr/bin/env python3
"""
test_utils.py

This module contains unit tests for the utils.get_json and utils.memoize.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json, memoize  # Ensurand match your utils module


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')  # Correct the patch target if needed
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize function."""

    def test_memoize(self):
        """Test that memoize caches the result of a method call."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()

        with patch.object(obj, 'a_method', return_value=42) as mock_method:
            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
