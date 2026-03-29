class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
    return dummy.next