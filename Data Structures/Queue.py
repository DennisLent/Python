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

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    def __len__(self):
        return self.__size

    def empty(self):
        return self.__head is None and self.__tail is None

    def push(self, item):
        if item is not None:
            if self.__head is None:
                self.__head = item

            elif self.__tail is None:
                self.__head.next = self.__tail
                self.__tail = item

            else:
                self.__tail.next = item
                item = self.__tail

            self.__size += 1

