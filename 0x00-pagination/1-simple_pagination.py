#!/usr/bin/env python3
"""Task 1: Simple pagination"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
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
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset.

        Args:
            page (int): The page number to return (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The paginated data for the specified page.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0, "page  integer >  0"
        assert isinstance(page_size, int) and page_size > 0, "page_size > 0"

        # Calculate start and end indexes
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset and return the appropriate page slice
        data = self.dataset()
        return data[start_index:end_index] if start_index < len(data) else []
