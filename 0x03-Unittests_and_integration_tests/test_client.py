#!/usr/bin/env python3
"""
test_client.py

This module contains unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient  # Ensure the correct path to the class
from utils import get_json  # Assuming get_json is in utils


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Set up the mock to return the expected response
        mock_get_json.return_value = expected_response
        
        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)
        
        # Call the .org property
        result = client.org
        
        # Ensure get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        
        # Assert that the result is as expected
        self.assertEqual(result, expected_response)


if __name__ == "__main__":
    unittest.main()
