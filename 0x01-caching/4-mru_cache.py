#!/usr/bin/python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class inherits from BaseCaching and is a caching system
        that uses the MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.mru_order = []  # List to track the order of usage

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm """
        if key is None or item is None:
            return

        # If the key is already in the cache, update the item and reorder
        if key in self.cache_data:
            self.cache_data[key] = item
            self.mru_order.remove(key)
            self.mru_order.append(key)
        else:
            # If the cache is full, discard the most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the most recently used key
                mru_key = self.mru_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add the new key-value pair to the cache
            self.cache_data[key] = item
            self.mru_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update the MRU order when the key is accessed
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
