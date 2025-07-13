#!/usr/bin/env python3
"""  Redis excercise file"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times
    a method is called using Redis INCR.
    """
    @wraps(method)
    def wrapper(seld, *args, **kwargs):
        redis_client = self._redis
        key = method.__qualname__
        redis_client.incr(key)
        return method(self, *args, kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of
    inputs and outputs of a method in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if isinstance(self._redis, redis.Redis):
            input_key = f"{method.__qualname__}: inputs"
            output_key = f"{method.__qualname__}: outputs"
            self._redis.rpush(input_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(output_key, str(result))
        return result
    return wrapper

def replay(method: Callable) -> None:
    """
    Display the history of calls for a given method.
    """
    if method is None or not hasattr(method, '__self__'):
        return
    redis_client = method.__self__._redis
    if isinstance(redis_client, redis.Redis):
        method_name = method.__qualname__
        input_key = f"{method_name}:inputs"
        output_key = f"{method_name}:outputs"

        count = redis_client.get(method_name)
        count = int(count.decode('utf-8')) if count else 0

        inputs = redis_client.lrange(input_key, 0, -1)
        outputs = redis_client.lrange(output_key, 0, -1)

        print(f"{method_name} was called {count} times:")

        for input_args, output in zip(inputs, outputs):
        # Decode bytes to string and format input as (*args,)
        input_str = input_args.decode('utf-8')
        print(f"{method_name}(*{input_str}) -> {output.decode('utf-8')}")

    

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
