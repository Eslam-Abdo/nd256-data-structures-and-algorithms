"""
1_lru_cache.py

For our first problem, the goal will be to design a data structure known as a
Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove
the least recently used entry when the cache memory reaches its limit.
For the current problem, consider both get and set operations as a use operation.

Your job is to ** use an appropriate data structure(s) to implement the cache **

    In case of a cache hit, your get() operation should return the appropriate value.
    In case of a cache miss, your get() should return -1.
    While putting an element in the cache, your put() / set() operation must insert the
    element. If the cache is full, you must write code that removes the least recently
    used entry first and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
Uses Pythons's OrderedDict as cache, which keeps track of the order that
entries are inserted. Deleting an entry and reinserting it will move it to the end.
If the value of a key is changed, the key position does not change.

Reference: https://docs.python.org/2/library/collections.html#collections.OrderedDict

Somewhat related implementation methodology (not in python)
https://www.geeksforgeeks.org/lru-cache-implementation/
"""
from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        if capacity < 1:
            print('LRUCache should have capacity > 0')
            return
        self.capacity = capacity
        self.element_num = 0
        self.cache = OrderedDict()

    def get_capacity(self):
        return self.capacity
    
    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        if key in self.cache.keys():
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        if key in self.cache.keys():
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(False)
                self.element_num -= 1
            self.cache[key] = value
            self.element_num += 1


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2
    pass

    # Test Case 3
    pass
