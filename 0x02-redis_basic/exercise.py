#!/usr/bin/env python3
"""This module defines a Cache class for interacting with Redis."""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Cache class for storing data in Redis."""

    def __init__(self) -> None:
        """Initialize the Cache instance and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key (e.g. using uuid), store the input
        data in Redis using the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve data from Redis and convert it using the provided function"""
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis."""
        data = self._redis.get(key)
        if data is None:
            return None
        return data.decode("utf-8")

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        data = self._redis.get(key)
        if data is None:
            return None
        try:
            return int(data.decode("utf-8"))
        except ValueError:
            return None
