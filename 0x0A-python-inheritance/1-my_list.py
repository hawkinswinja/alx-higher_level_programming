#!/usr/bin/python3
"""my_list module
   contains one function
"""


class MyList(list):
    """MyList is a subclass of list
       it inherits all attributes associated with list
    """
    def print_sorted(self):
        """prints the list in sorted order without affecting original list
           returns a sorted list
        """
        a = self.copy()
        a.sort()
        print(a)
