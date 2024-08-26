#!/usr/bin/env python3
"""
test_utils.py

This module contains unit tests for the utils.get_json function.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result."""
        # Create a mock response object with a .json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with the test_url
        result = get_json(test_url)

        # Assert that the mock_get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result is equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
