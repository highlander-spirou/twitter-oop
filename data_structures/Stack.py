from typing import Optional, Literal


class Node:
    data = None
    next_node:Optional["Node"] = None
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def get_data_attr(self, attr, type_of:Literal['dict', 'other']='dict'):
        if type_of == 'dict':
            return self.data.get(attr)
        else:
            return getattr(attr, self.data)

class StackIterator:
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

class Stack:
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

    
    def get_nth_node(self, index:int, primer:Optional[Node]=None) -> Optional[Node]:
        """
        Traverse the stack to the nth node (zero-indexed).
        Provision of primer node to reduce the time complexity

        ie. Traverse from head -> 1000th will cost 999, while traverse from 990 to 1000 will cost 9
        """
        current_node = self.head if primer is None else primer
        i = 0
        while current_node:
            if i == index:
                return current_node
            else:
                i += 1
                current_node = current_node.next_node


    def __iter__(self):
        return StackIterator(self.head)

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
    l1 = Stack()
    l1.add(1) # 4
    l1.add(2) # 3
    l1.add(3) # 2
    l1.add(4) # 1
    l1.add(5) # 0


   
    # l2 = Stack()
    # l2.add(2) # 4
    # l2.add(4) # 3
    # l2.add(6) # 2
    # l2.add(8) # 1

    # l3 = Stack()
    # l3.add(1) # 4
    # l3.add(2) # 3
    # l3.add(3) # 2
    # l3.add(5) # 1
    # l3.add(7) # 1
    # l3.add(9) # 1

    # print(l1, l2, l3, sep = " | ")




