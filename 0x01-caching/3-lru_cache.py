#!/usr/bin/env python3
""" LRUCache module """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching
        Implements a caching system with an LRU policy.
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()  # Call the parent class's constructor
        self.cache_data = OrderedDict()  # Method to maintain the orderOfUsage

    def put(self, key, item):
        """ Add an item in the cache using LRU policy """
        if key is None or item is None:
            return  # Do nothing if either key or item is None

        # If key is already in the cache, remove it to update its position
        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If cache is full, discard the least recently used item
            discarded_key = next(iter(self.cache_data))  # Get the firstkey
            print(f"DISCARD: {discarded_key}")  # Print the discarded key
            self.cache_data.pop(discarded_key)  # Remove LRU item from cache

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None  # Return None if the key is None or not in cache

        # Move the accessed item to the end to mark it as recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
