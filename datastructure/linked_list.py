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

    def __str__(self):
        """Return Full Linked List"""
        tmp = self.head

        print_str = "head ->> "
        while tmp:
            print_str += f"{tmp.data} ->> "
            tmp = tmp.next
        print_str += " None"
        return print_str

    def __len__(self):
        """Return length of the lisked list"""
        count = 0
        tmp = self.head

        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def getCountRec(self, node):
        if not node:
            return 0
        return 1 + self.getCountRec(node.next)

    def getCount(self):
        tmp = self.head
        print("Length rec: ", self.getCountRec(tmp))

    def searchIter(self, key):
        tmp = self.head
        while tmp:
            if tmp.data == key:
                print(f"{key} is found")
                return
            tmp = tmp.next
        print(f"{key} not found")

    def searchRec(self, node, key):
        if not node:
            return False
        if node.data == key:
            return True
        return self.searchRec(node.next, key)

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverseRec(self, node):
        if not node or not node.next:
            return node

        rest = self.reverseRec(node.next)

        node.next.next = node
        node.next = None

        return rest


if __name__ == "__main__":
    li = LinkedList()

    li.push(40)
    li.push(30)
    li.append(88)
    li.append(99)
    li.push(20)
    li.insertAfter(li.head.next, 99)
    li.push(10)

    li.getCount()
    print("Length: ", len(li))
    print(li)

    li.searchIter(88)
    if li.searchRec(li.head, 99):
        print("Key found")
    else:
        print("Key not found")

    li.reverse()
    print(li)
    li.head = li.reverseRec(li.head)
    print(li)
