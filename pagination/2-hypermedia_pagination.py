#!/usr/bin/env python3

"""return a tuple of size two containing
a start index and an end index"""

from typing import Tuple
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing
    a start index and an end index corresponding"""
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
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the page to find in the file and return it"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        file = self.dataset()
        start, end = index_range(page, page_size)
        if len(file) < end:
            return []
        data = file[start:end]

        return data
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """returns a dictionary of a file
        that contains information about it"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        file = self.dataset()
        total_pages = math.ceil(len(file) / page_size)
        if page + 1 != total_pages + 1:
            next_page = page + 1
        else:
            next_page = None
        if page - 1 < 1:
            prev_page = None
        else:
            prev_page = page - 1
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
