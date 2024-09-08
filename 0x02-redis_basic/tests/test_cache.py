#!/usr/bin/env python3

"""Test cases for the Cache class."""

import unittest
import redis
from exercise import Cache


class TestCache(unittest.TestCase):
    """Test cases for the Cache class."""

    def setUp(self):
        """Set up a new Cache instance before each test."""
        self.cache = Cache()

    def test_store_and_get(self):
        """Test storing and retrieving data."""
        data = b"hello"
        key = self.cache.store(data)
        self.assertEqual(self.cache.get(key), data)

    def test_get_str(self):
        """Test retrieving data as a string."""
        data = "world"
        key = self.cache.store(data)
        self.assertEqual(self.cache.get_str(key), data)

    def test_get_int(self):
        """Test retrieving data as an integer."""
        data = 42
        key = self.cache.store(data)
        self.assertEqual(self.cache.get_int(key), data)

    def test_non_existent_key(self):
        """Test retrieving data from a non-existent key."""
        self.assertIsNone(self.cache.get("nonexistent_key"))
        self.assertIsNone(self.cache.get_str("nonexistent_key"))
        self.assertIsNone(self.cache.get_int("nonexistent_key"))

    def test_get_with_conversion_function(self):
        """Test retrieving data with a custom conversion function."""
        data = b"custom_conversion"
        key = self.cache.store(data)
        self.assertEqual(self.cache.get(
            key, fn=lambda d: d.decode("utf-8")), data.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()
