class Btree(object):
    """
    The base class for the b-tree data structure
    It is initialized with an integer specifying its order.
    """

    def __init__(self, order: int) -> None:
        if type(order) is int:
            self.order = order
        else:
            raise TypeError("Cannot allocate size as a non-integer")
        
        self.root = Node(num_keys = (2 * self.order - 1) )
        

        
class NodeKey(object):
    """
      The base class for keys
    """

    def __init__(self, idx:int, content:list[tuple]):
        self.idx = idx 
        self.content = dict(content) 


class Node(object):
    """
    The base class for node objects
    """

    def __init__(self, num_keys:int) -> None:
        self.is_leaf = True 
        self.is_full = False 
        self.num_keys = num_keys
        self.keys = []
        self.children: list[Node]

    def update_state(self):
        if len(self.keys) == self.num_keys:
            self.is_full = True 
    
    def insert_key(self, key:NodeKey) -> int:
        if not self.is_full:
            self.keys.append(key)
            return 0
        else:
            return 1
        