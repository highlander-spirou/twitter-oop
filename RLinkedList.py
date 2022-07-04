from optparse import Option
from re import I
from typing import List, Optional


class Node:
    data = None
    next_node:Optional["Node"] = None
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

class LinkedListIterator:
    def __init__(self, head:Node):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            returned_node = self.current
            self.current = self.current.next_node
            return returned_node

class ReverseLinkedList:
    """
    This class implement a reverse linked list, aka a stack
    that an element only being insert at the top of the list
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.count: int = 0

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        old_head = None
        if self.is_empty():
            self.head = new_node
            self.count += 1
        else:
            old_head = self.head
            self.head = new_node
            self.head.next_node = old_head
            self.count += 1

    
    def traverse_at_n(self, n:int) -> Optional[Node]:
        """
        Get the element at nth position
        with "n" is the index (0-based) 
        """
        if n == 0:
            return self.head
        elif n < self.count:
            nth_node = self.head
            i = 1
            while i < self.count and i < n+1:
                if nth_node is not None:
                    nth_node = nth_node.next_node
                else: 
                    break
                i += 1
            return nth_node
        else: 
            raise Exception("Index out of range")

    def traverse_to_n(self, start:int, stop:int) -> Optional[List[Node]]:
        returned_list:List[Node] = []
        i = start
        current = self.traverse_at_n(start)
        if current is None:
            return returned_list if len(returned_list) > 0 else None
        while i <= stop:
            returned_list.append(current)
            i+=1
            current = current.next_node
        return returned_list

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __repr__(self):
        nodes = []
        i = 0
        current = self.head
        while i < self.count:
            nodes.append(str(current))
            current = current.next_node
            i+=1

        return ' -> '.join(nodes)



if __name__ == '__main__':
    l1 = ReverseLinkedList()
    l1.add(1) # 4
    l1.add(2) # 3
    l1.add(3) # 2
    l1.add(4) # 1
    l1.add(5) # 0


    for i in l1.traverse_to_n(1, 3):
        print(i)
    # l2 = ReverseLinkedList()
    # l2.add(2) # 4
    # l2.add(4) # 3
    # l2.add(6) # 2
    # l2.add(8) # 1

    # l3 = ReverseLinkedList()
    # l3.add(1) # 4
    # l3.add(2) # 3
    # l3.add(3) # 2
    # l3.add(5) # 1
    # l3.add(7) # 1
    # l3.add(9) # 1

    # print(l1, l2, l3, sep = " | ")




