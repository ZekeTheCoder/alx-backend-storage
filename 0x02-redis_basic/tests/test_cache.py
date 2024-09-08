#!/usr/bin/env python3

"""Test cases for the Cache class."""

import unittest
import redis
from exercise import Cache


def byte_to_str(byte_data):
    """Convert byte data to a UTF-8 string."""
    return byte_data.decode("utf-8")


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
            key, fn=byte_to_str), data.decode("utf-8"))
        # self.assertEqual(self.cache.get(
        #     key, fn=lambda d: d.decode("utf-8")), data.decode("utf-8"))

    def test_count_calls(self):
        """Test that the count_calls decorator works as expected."""
        # Store some values
        self.cache.store(b"first")
        self.cache.store(b"second")
        self.cache.store(b"third")
        self.cache.store(b"fourth")

        # Check if the count is correct
        call_count = self.cache.get(self.cache.store.__qualname__)
        self.assertEqual(call_count, b'4')  # We called store 4 times


if __name__ == '__main__':
    unittest.main()
