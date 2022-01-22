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

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data


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

    def __min__(self):
        return self.smallest()

    def __max__(self):
        return self.greatest()

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

    def __iter__(self):
        self.__current = self.get_first()
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration()

        result = self.__current
        self.__current = self.__current.next
        return result

    def search(self, key):
        result = None
        for node in self:
            if key == node.data:
                result = node
        return result

    def remove(self, key):
        node = self.search(key)
        if node is not None:
            prev_node = node.prev
            next_node = node.next

            if prev_node is not None:
                prev_node.next = next_node
            else:
                self.__head = next_node

            if next_node is not None:
                next_node.prev = prev_node
            else:
                self.__tail = prev_node

        self.__size -= 1

    def smallest(self):
        sml = self.get_first()
        for item in self:
            if item < sml:
                sml = item
        return sml.data

    def greatest(self):
        grt = self.get_first()
        for item in self:
            if item > grt:
                grt = item
        return grt.data







my_list = DoublyLinkedList()
print(f"my list: {str(my_list)}")
print(f"list empty? {my_list.empty()}")
for num in [i for i in range(0, 100, 7)]:
    my_list.add(num)

print(f"my list: {str(my_list)}")
print(f"my list is {my_list.size()} Nodes long")

for num in [21, 42, 63, 77, "x", None]:
    my_list.remove(num)

print(f"my list after removing: {str(my_list)}")

print(f"smallest: {min(my_list)}")

print(f"greatest: {max(my_list)}")


