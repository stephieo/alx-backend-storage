#!/usr/bin/env python3
"""  Redis excercise file"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(seld, *args, **kwargs):
        redis_client = self._redis
        key = method.__qualname__
        redis_client.incr(key)
        return method(self, *args, kwargs)
    return wrapper

class Cache():
    """ Defines a Cache class to interact with Redis """
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data in Redis with key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: [Callable]):
        """get method"""

        if (fn is None):
            value = self._redis.get(key)
        elif (type(key) isinstance(str)):
            value = self.get_str(key)
        elif (type(key) isinstance(int)):
            value = get_int(key)

        if (value is None):
            return None
        else:
            print(type(value))
            return value

    def get_str(self, key: str):
        """convert byte string to UTF-8 string"""
        value = self._redis.get(key).decode("utf-8")
        return value

    def get_int(self, key: int):
        """convert byte string to integer"""
        value = self._redis.get(key)
        return (int.from_bytes(value))
