#!/usr/bin/env python3
""" Test Client """
import unittest
from unittest.mock import patch
from parameterized import parameterized
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test GitHub Org Client Class """
    def __init__(self):
        self.gitHub_client_obj = GithubOrgClient()

    @parameterized.expend([
        ("google"),
        ("abc"),
    ])
    @patch("get_json")
    def test_org(self, param_arg, mock_get):
        """ Test that GithubOrgClient.org returns the correct value """
        pass
