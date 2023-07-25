#!/usr/bin/env python3
"""A simple pagination helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Pagination method"""
    if page and page_size:
        if page > 0:
            if page == 1:
                return (page - 1, page_size)
            else:
                return ((page - 1) * page_size, page * page_size)
        else:
            return
    return
