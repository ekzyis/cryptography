"""Utility class to store bitstrings in a more readable way."""

from itertools import chain
from typing import List, Any

from util.concat_bits import concat_bits
from util.split import split


class Word(int):
    # TODO args should actually be hinted with Union[int, Tuple[int, ...]]
    def __new__(cls, *args: Any, bit: int = 32) -> 'Word':
        """Creates an actual integer out of the word representation given with args and bit."""
        _args: List[Any] = list(args)
        if isinstance(args[0], tuple):
            _args = [a for a in chain(*args)]
        # TODO mypy throws error: Too many arguments for "__new__" of "object"
        return int.__new__(cls, concat_bits(*_args, n=bit))

    def __init__(self, *args: Any, bit: int = 32) -> None:
        """Constructor which saves the passed-in attributes for later usage."""
        super().__init__()
        self.blocks = args
        self.bit = bit

    def __iter__(self):
        """Returns an iterator to the blocks of bytes."""
        return split(len(self.blocks), self.bit, self).__iter__()
