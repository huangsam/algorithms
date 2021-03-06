import pytest

from algorithms.list.reverse_list import reverse_list


@pytest.mark.list
def test_reverse_list(sorted_list):
    prev_node = None
    cur_node = sorted_list
    new_node = reverse_list(sorted_list)
    assert cur_node != new_node
    while cur_node:
        if prev_node:
            assert cur_node.value < prev_node.value
        prev_node = cur_node
        cur_node = cur_node.next_node
