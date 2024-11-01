#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
        Implements a caching system with a LIFO policy.
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()  # Call the parent class's constructor
        self.last_key = None  # Track the last key added

    def put(self, key, item):
        """ Add an item to the cache using LIFO policy """
        if key is not None and item is not None:
            self.cache_data[key] = item  # Add or update the key-value pair
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key:
                    del self.cache_data[self.last_key]  # Delete the last key
                    print(f"DISCARD: {self.last_key}")
            self.last_key = key  # Update the last key added

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key)  # Return the item if found, else None
