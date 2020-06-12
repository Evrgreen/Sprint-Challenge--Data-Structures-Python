class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def __str__(self):
        # current = self.head
        # while current:
        #     print(current)
        #     current = current.next_node
        # return str(self.head.value)
        return f'{str(self.head.value)} {str(self.head.next_node.value)}{str(self.head.next_node.next_node.value)} {str(self.head.next_node.next_node.next_node.value)}'

    def reverse_list(self, node, prev):
        if prev is not None:
            if not prev.next_node:
                prev.set_next(node)
                self.head = prev
            else:
                self.reverse_list(prev, prev.next_node)
            prev.set_next(node)
        elif node and node.next_node:
            self.reverse_list(node, node.next_node)


test_list = LinkedList()
test_list.add_to_head(1)
test_list.add_to_head(2)
test_list.add_to_head(3)
test_list.add_to_head(4)
test_list.add_to_head(5)

print(test_list)
test_list.reverse_list(test_list.head, test_list.head.next_node)
print(test_list)
