#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for pagination

    Args:
        page: The page number (1-indexed)
        page_size: The number of items per page

    Returns:
        A tuple containing (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset

        Args:
            page: The page number (1-indexed)
            page_size: The number of items per page

        Returns:
            List of rows for the requested page
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the range for this page
        start, end = index_range(page, page_size)

        # Get the dataset
        data = self.dataset()

        # Return the slice, or empty list if out of range
        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get hypermedia pagination information

        Args:
            page: The page number (1-indexed)
            page_size: The number of items per page

        Returns:
            Dictionary with pagination metadata
        """
        # Get the data for this page using get_page
        data = self.get_page(page, page_size)

        # Calculate total pages
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # Determine next_page
        next_page = page + 1 if page < total_pages else None

        # Determine prev_page
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
