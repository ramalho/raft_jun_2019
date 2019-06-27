import pytest

from log import Log, Entry
from log import InvalidTerm, NegativeIndex, IndexBeyondLast


def test_append_to_empty():
    l = Log()

    new_entries = [Entry(1, 'first')]
    l.append(0, 1, new_entries)

    assert l.entries == [None] + new_entries


def test_append_prev_index_is_negative():
    l = Log()

    new_entries = [Entry(1, 'first')]

    with pytest.raises(NegativeIndex):
        l.append(-1, 1, new_entries)


def test_append_beyond_last():
    l = Log()

    new_entries = [Entry(1, 'first')]

    with pytest.raises(IndexBeyondLast):
        l.append(1, 1, new_entries)


def test_append_to_not_empty():
    initial_entries = [Entry(1, 'first')]
    l = Log(initial_entries)

    new_entries = [Entry(1, 'second')]
    l.append(1, 1, new_entries)

    assert l.entries == [None] + initial_entries + new_entries


def test_append_to_not_empty_beyond_last():
    initial_entries = [Entry(1, 'first')]
    l = Log(initial_entries)

    new_entries = [Entry(1, 'second')]
    with pytest.raises(IndexBeyondLast):
        l.append(2, 1, new_entries)


def test_append_wrong_term():
    initial_entries = [Entry(1, 'first')]
    l = Log(initial_entries)

    new_entries = [Entry(2, 'second')]
    with pytest.raises(InvalidTerm):
        l.append(1, 2, new_entries)


def test_append_ovewrite():
    initial_entries = [Entry(1, 'first'), Entry(1, 'second')]
    l = Log(initial_entries)

    new_entries = [Entry(1, 'third')]
    l.append(1, 1, new_entries)

    assert l.entries == [None] + initial_entries[:1] + new_entries
