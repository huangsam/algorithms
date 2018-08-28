import pytest

from collection.list import ListNode


@pytest.fixture
def sorted_list(request):
    head = ListNode(0)
    node = head
    for i in range(1, 6):
        node.next_node = ListNode(i)
        node = node.next_node
    return head


class TestList(object):

    def test_list_is_sorted(self, sorted_list):
        prev_node = None
        cur_node = sorted_list
        while cur_node:
            if prev_node:
                assert cur_node.value > prev_node.value
            prev_node = cur_node
            cur_node = cur_node.next_node

    def test_list_is_unsorted(self, sorted_list):
        prev_node = None
        cur_node = ListNode(99)
        cur_node.next_node = sorted_list
        is_unsorted = False
        while cur_node:
            if prev_node:
                is_unsorted = True
            prev_node = cur_node
            cur_node = cur_node.next_node
        assert is_unsorted
