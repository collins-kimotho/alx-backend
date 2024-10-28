#!/usr/bin/env python3
"""Task 1: Simple pagination"""


import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get hypermedia pagination information.

        Args:
            page (int): The page number to return (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Optional[int]]: Pagination information for hypermedia.
        """
        # Get data for the current page
        data = self.get_page(page, page_size)

        # Calculate total pages
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # Define next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Construct pagination metadata
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
