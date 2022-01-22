class Node:
    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def __str__(self):
        return f"{self.__data}"

    def get_next(self):
        return self.__next

    def set_next(self, item):
        self.__next = item

    def get_prev(self):
        return self.__prev

    def set_prev(self, item):
        self.__prev = item

    def get_data(self):
        return self.__data

    def set_data(self, item):
        self.__data = item

    next = property(get_next, set_next)

    prev = property(get_prev, set_prev)

    data = property(get_data, set_data)


class DoublyLinkedList:
    """
    Doubly Linked List that is none terminated
    Empty if head and tail are None
    """
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        return_string = "|"
        node = self.get_first()
        while node is not None:
            return_string += f"-{node}"
            node = node.next
        return return_string + "|"

    def get_first(self):
        return self.__head

    def get_last(self):
        return self.__tail

    def empty(self):
        return self.__head is None and self.__tail is None

    def size(self):
        return self.__size

    def add(self, item):
        if item is not None:
            node = Node(item)
            if self.empty():
                self.__head = node
            else:
                node.prev = self.__tail
                self.__tail.next = node
            self.__tail = node
            self.__size += 1







my_list = DoublyLinkedList()
print(f"my list: {str(my_list)}")
print(f"list empty? {my_list.empty()}")
for num in [1,2,3,4,5,6]:
    my_list.add(num)

print(f"my list: {str(my_list)}")
print(f"my list is {my_list.size()} Nodes long")
print(my_list.get_first())
print(my_list.get_last().prev)

