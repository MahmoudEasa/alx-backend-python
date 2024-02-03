#!/usr/bin/env python3
""" Test Client """
import unittest
from unittest.mock import patch
from parameterized import parameterized
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test GitHub Org Client Class """

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get):
        """ Test that GithubOrgClient.org returns the correct value """

        obj = GithubOrgClient(org_name)
        obj.org()
        mock_get.assert_called_once_with(expected)
