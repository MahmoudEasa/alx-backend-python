#!/usr/bin/env python3
""" Test Client """
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

@parameterized_class(("org_payload", "repos_payload",
                     "expected_repos", "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration GithubOrgClient """

    @classmethod
    def setUpClass(cls):
        """ Set Up Class """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
                    Mock(json=Mock(return_value=cls.org_payload)),
                    Mock(json=Mock(return_value=cls.repos_payload)),
                ]

        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """ Tear Down Class """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Method to unit-test GithubOrgClient.public_repos """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Method to Test Public Repos With License """
        self.assertEqual(self.client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
