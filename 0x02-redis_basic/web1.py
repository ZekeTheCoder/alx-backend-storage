#!/usr/bin/env python3
"""building web cache and tracker implementation using Redis."""
import redis
import requests
from typing import Callable

redis_connection = redis.Redis()


def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and cache it for 10 seconds
                and track the number of times the URL was accessed.
    """
    cache_key = f"cached:{url}"
    count_key = f"count:{url}"

    cached_content = redis_connection.get(cache_key)
    if cached_content:
        return cached_content.decode('utf-8')

    # If not cached, fetch the content
    response = requests.get(url)
    html_content = response.text
    redis_connection.setex(cache_key, 10, html_content)
    redis_connection.incr(count_key)

    return html_content


def access_count(url: str) -> int:
    """Retrieve the access count for a given URL."""
    count_key = f"count:{url}"
    count = redis_connection.get(count_key)
    return int(count) if count else 0


# if __name__ == "__main__":
#     # print(access_count("https://httpbin.org/delay/5"))
#     url = "https://httpbin.org/delay/5"
#     print(f"First access: {get_page(url)}")
#     print(f"Access count: {access_count(url)}")
#     # print(f"Second access: {get_page(url)}")
#     # print(f"Access count: {access_count(url)}")
