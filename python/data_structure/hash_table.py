import unittest
from abc import ABC, abstractmethod


class InnerHashTable(ABC):
    @abstractmethod
    def hash(self, key) -> int: ...

    @abstractmethod
    def put(self, key, value) -> bool: ...

    @abstractmethod
    def get(self, key) -> str: ...

    @abstractmethod
    def delete(self, key) -> bool: ...

    @abstractmethod
    def print_all(self): ...


class HashTable(InnerHashTable):
    def __init__(self):
        ...

    class Node:
        def __init__(self, capacity):
            ...


class HashTableTest(unittest.TestCase):
    def set_up(self):
        ...

    def test_put(self):
        ...

    def test_get(self):
        ...

    def test_delete(self):
        ...

    def test_print_all(self):
        ...
