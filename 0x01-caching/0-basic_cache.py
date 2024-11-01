#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
        A simple caching system without any limit on the number of items.
    """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item  # Store the item in the cache

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key)  # Return the item if found, else None