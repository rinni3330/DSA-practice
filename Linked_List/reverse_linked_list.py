def linked_list(self):

    class Node(self):
        def __init__(self, data):
            self.data = data
            self.next = next
    
    def reverse_linked_list(head):
        prev = None
        current = head
        while current:
            New_node = current.next
            current.next = prev
            prev = current
            current = New_node
        return prev
