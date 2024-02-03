#!/usr/bin/env python3
""" Test Client """
import unittest
from unittest.mock import patch, PropertyMock
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
        obj.org
        mock_get.assert_called_once_with(expected)

    @patch("client.GithubOrgClient.org")
    def test_public_repos_url(self, mock_repos):
        """ Method to unit-test GithubOrgClient._public_repos_url """

        mock_repos.return_value = {"repos_url": "url"}
        obj = GithubOrgClient("repos_url")

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = mock_repos.return_value["repos_url"]
            result = obj._public_repos_url

        self.assertEqual(result, "url")
