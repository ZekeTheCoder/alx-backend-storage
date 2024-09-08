#!/usr/bin/env python3

"""Test script for Cache class."""

from exercise import Cache


def main():
    """Main function to test Cache class functionality."""
    cache = Cache()

    TEST_CASES = {
        b"foo": None,  # Expected to be retrieved as bytes
        123: int,      # Expected to be retrieved as integer
        # Expected to be retrieved as a UTF-8 string
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        # Store the value in Redis
        key = cache.store(value)

        # Retrieve the value and apply the conversion function
        retrieved_value = cache.get(key, fn=fn)

        # Assert that the retrieved value matches the original value
        assert retrieved_value == value, f"Failed for key: {key}. Expected: {value}, Got: {retrieved_value}"

    print("All tests passed!")


if __name__ == "__main__":
    main()
