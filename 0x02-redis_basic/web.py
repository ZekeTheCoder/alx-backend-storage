#!/usr/bin/env python3
"""building web cache and tracker implementation using Redis."""
import redis
import requests
from functools import wraps

redis_client = redis.Redis()


def cache_decorator(method):
    """Decorator to cache the result of the function for 10 seconds."""
    @wraps(method)
    def wrapper(url: str):
        cached_content = redis_client.get(f"cached:{url}")
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch the content if not cached
        content = method(url)
        redis_client.setex(f"cached:{url}", 10, content)
        return content

    return wrapper


@cache_decorator
def get_page(url: str) -> str:
    """Fetch HTML content of a URL and track the number of accesses."""
    count = redis_client.incr(f"count:{url}")
    content = requests.get(url).text
    print(f"Access count: {count}")
    return content


if __name__ == "__main__":
    # url = "http://slowwly.robertomurray.co.uk"
    url = "https://httpbin.org/delay/10"
    print(f"First access: {get_page(url)}")
    print(f"Second access: {get_page(url)}")
