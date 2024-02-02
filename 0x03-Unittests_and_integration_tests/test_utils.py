#!/usr/bin/env python3
""" Create a TestAccessNestedMap class that inherits from unittest.TestCase
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Class to Test utils.access_nested_map function """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test that a KeyError is raised """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test that utils.get_json returns the expected result """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test that utils.get_json returns the expected result """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        res = get_json(test_url)
        mock_get.assert_called_with(test_url)
        self.assertEqual(res, test_payload)


if __name__ == "__main__":
    unittest.main()
