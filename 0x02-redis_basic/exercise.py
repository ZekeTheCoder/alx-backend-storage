#!/usr/bin/env python3

"""This module defines a Cache class for interacting with Redis."""

import redis
import uuid
from typing import Union


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
