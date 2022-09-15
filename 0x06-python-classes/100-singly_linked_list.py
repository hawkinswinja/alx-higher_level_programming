#!/usr/bin/python3
""" creating a singly linked list"""


class Node:
    """node of a list.
       @args
            data: integer value
            next_node: pointer to the next node"""

    def __init__(self, data, next_node=None):
        """class constructor. initializes class instances"""
        if (not isinstance(data, int)):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieve data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """update content of the node's data"""
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """pointer to the next node in the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """update the next node in the list"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """creates a single linked list
       @args:
            head: pointer to the list
    """
    def __init__(self):
        """initializes the class"""
        self.__head = None

    def sorted_insert(self, value):
        """adds data to the list in ascending order"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """add next line after each character of the singly linked list"""
        mylist = []
        tmp = self.__head
        while (tmp is not None):
            mylist.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(mylist))
