#!/usr/bin/env python3

""" intro to caching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A class that inherits from a BaseCaching class"""
    def put(self, key, item):
        """ adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item by key """
        return self.cache_data.get(key, None)
