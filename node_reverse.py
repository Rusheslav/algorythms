
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next_node = None
        self.previous_node = None

    def __str__(self):
        return self.value

class Linked_list:
    def __init__(self):
        self.head = None
        # self.tail = None

    def find_node(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next_node
        return None

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def insert_node(self, value, previous_node):
        new_node = Node(value)
        previous_node = self.find_node(previous_node)
        if previous_node is None:
            self.add_to_end(value)
            return
        last_node = previous_node.next_node
        previous_node.next_node = new_node
        new_node.next_node = last_node

    def print_linked_list(self):
        node = self.head
        if node is None:
            return "Linked list is empty"
        result = ""
        while node:
            result += f"{node.__str__()}" + " "
            node = node.next_node
        return result

    def del_head(self):
        if self.head:
            self.head = self.head.next_node
        else:
            raise Exception("Linked list is empty")

    def del_end(self):
        node = self.head
        if node is None or node.next_node is None:
            self.head = None
            return
        old_node = None
        while node.next_node:
            old_node = node
            node = node.next_node
        old_node.next_node = None

    def reverse_list(self):
        previous_node = None
        node = self.head
        if node is None:
            print("Linked list is empty")
            return
        next_node = node.next_node
        while node:
            node.next_node = previous_node
            previous_node = node
            node = next_node
            if next_node:
                next_node = node.next_node
        self.head = previous_node


a = Linked_list()
a.add_to_end(12)
a.add_to_end(10)
a.add_to_end(11)
print(a.print_linked_list())
# a.del_head()
a.insert_node(19, 10)
print(a.print_linked_list())
a.reverse_list()
print(a.print_linked_list())
