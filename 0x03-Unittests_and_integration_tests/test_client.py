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

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """ Method to unit-test GithubOrgClient.public_repos """

        mock_get.return_value = [
                {"name": "value1"},
                {"name": "value2"}
            ]

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = "url"
            list_repos = GithubOrgClient("name").public_repos()

        self.assertEqual(list_repos, ["value1", "value2"])
        mock_get.assert_called_once_with("url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Method to unit-test GithubOrgClient.has_license """
        result = GithubOrgClient("name").has_license(repo, license_key)
        self.assertEqual(result, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration GithubOrgClient """
    def setUpClass():
        """ Set Up Class """
        pass

    def tearDownClass():
        """ Tear Down Class """
        pass

    @patch("client.get_json")
    def test_public_repos_with_license(self, mock_get):
        """ Method to test the public_repos
            with the argument license='apache-2.0'
        """
        mock_get.return_value = [
                {"name": "value1"},
                {"name": "value2"}
            ]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = "url"
            list_repos = GithubOrgClient("name").public_repos("apache-2.0")

        self.assertEqual(list_repos, [])
        mock_get.assert_called_once_with("url")
