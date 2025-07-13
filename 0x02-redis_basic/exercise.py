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


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if isinstance(self._redis, redis.Redis)
            input_key = f"{method.__qualname__}:inputs"
            output_key = f"{method.__qualname__}:outputs"
            self._redis.rpush(input_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(output_key, str(result))
        return result
    return wrapper

class Cache():
    """ Defines a Cache class to interact with Redis """
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
