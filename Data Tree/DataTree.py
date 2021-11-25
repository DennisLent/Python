class Node:

    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def get_left(self):
        return self.__left

    def set_left(self, item):
        self.__left = item

    left = property(get_left, set_left)

    def get_right(self):
        return self.__right

    def set_right(self, item):
        self.__right = item

    right = property(get_right, set_right)

    def get_data(self):
        return self.__data

    def set_data(self, item):
        self.__data = item

    data = property(get_data, set_data)

    def __str__(self):
        return f"Node: {self.__data}"


class Tree:
    pass
