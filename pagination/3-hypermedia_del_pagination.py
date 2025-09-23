#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page of data with deletion-resilient pagination

        Args:
            index: The start index for the page
            page_size: The number of items per page

        Returns:
            Dictionary with index, next_index, page_size, and data
        """
        # Get the indexed dataset
        indexed_data = self.indexed_dataset()

        # Set default index if None
        if index is None:
            index = 0

        # Assert that index is in valid range
        assert 0 <= index < len(self.dataset()), "Index out of range"

        # Collect the page data
        data = []
        current_index = index
        collected = 0

        # Keep looking for items until we have page_size items or run
        # out of data
        while (collected < page_size and
               current_index < max(indexed_data.keys()) + 1):
            # Check if this index exists (hasn't been deleted)
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        # Set next_index to the current position after collecting
        # page_size items
        next_index = current_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
