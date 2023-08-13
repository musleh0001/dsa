class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Insert at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """Insert after a given node"""
        if prev_node is None:
            print("The given previous can't be None")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        """Insert at the end"""
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        _last = self.head
        while _last.next:
            _last = _last.next

        _last.next = new_node

    def printf(self):
        tmp = self.head

        print(f"head ->> ", end="")
        while tmp:
            print(tmp.data, end=" ->> ")
            tmp = tmp.next
        print("None")


if __name__ == "__main__":
    li = LinkedList()

    li.push(40)
    li.push(30)
    li.append(88)
    li.append(99)
    li.push(20)
    li.insertAfter(li.head.next, 99)
    li.push(10)

    li.printf()
