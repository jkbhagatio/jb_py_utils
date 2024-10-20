"""Random utility functions."""

from collections import OrderedDict

class OrderedSet:
    """An ordered hash set. 
    
    Uses OrderedDict to maintain the order of elements added to a set.
    """
    def __init__(self):
        self._dict = OrderedDict()

    def add(self, item):
        self._dict[item] = None

    def values(self):
        return list(self._dict.keys())
    
    def __getitem__(self, index):
        return self.values()[index]

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def __repr__(self):
        return self.values().__repr__()
