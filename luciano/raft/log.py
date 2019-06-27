
from collections import namedtuple

Entry = namedtuple('Entry', 'term data')

class InvalidTerm(Exception):
    pass

class NegativeIndex(Exception):
    pass

class IndexBeyondLast(Exception):
    pass



class Log:

    def __init__(self, entries=None):
        self.entries = [None]  # make log index start at 1
        if entries:
            self.entries.extend(entries)

    def append(self, prev_index, prev_term, entries):
        if prev_index < 0:
            raise NegativeIndex()
        if prev_index >= len(self.entries):
            raise IndexBeyondLast()
        if (prev_index >= 1 and
            self.entries[prev_index].term != prev_term):
            raise InvalidTerm
        self.entries[prev_index + 1:] = entries
