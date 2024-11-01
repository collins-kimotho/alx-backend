#!/usr/bin/env python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
        Implements a caching system with a FIFO policy.
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()  # Call the parent class's constructor
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """ Add an item to the cache using FIFO policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)  # Remove the key if it already exists
            self.cache_data[key] = item  # Add or update the key-value pair
            self.order.append(key)  # Record the order of this key

            # If the cache exceeds the max size, discard the oldest item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)  # Remove the first key added
                del self.cache_data[oldest_key]  # Delete it from the cache
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key)  # Return the item if found, else None
