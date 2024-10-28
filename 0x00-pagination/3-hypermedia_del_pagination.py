#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads the dataset if it hasn't been loaded already."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict:
        """Creates an indexed version of the dataset for
        deletion-resilient access
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]  # Limit to the first 1000 rows
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Returns a deletion-resilient page of the dataset.
        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items per page.
        Returns:
            Dict: A dictionary containing page data and metadata.
        """
        # Assertions to ensure that index and page_size are valid
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        # Retrieve the indexed dataset
        indexed_data = self.indexed_dataset()
        dataset_size = len(indexed_data)

        # Initialize variables for the output data collection
        data = []
        current_index = index
        items_collected = 0

        # Collect exactly `page_size` items, skipping deleted items if any
        while items_collected < page_size and current_index < dataset_size:
            # Check if the current index is in the indexed dataset
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_collected += 1
            current_index += 1

        # The next index will be the `current_index` where we stopped
        next_index = current_index if current_index < dataset_size else None

        # Build and return the dictionary with page information
        return {
            "index": index,          # Starting index for the page
            "next_index": next_index,  # The next index to continue pagination
            "page_size": len(data),   # Actual size of the page
            "data": data              # Page data itself
        }
