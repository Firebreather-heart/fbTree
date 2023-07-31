class BTreeNode:
    def __init__(self, is_leaf=True):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def is_full(self):
        return len(self.keys) == 5

class BTree:
    def __init__(self):
        self.root = BTreeNode(is_leaf=True)

    def insert(self, key):
        if self.root.is_full():
            new_root = BTreeNode(is_leaf=False)
            new_root.children.append(self.root)
            self._split(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _split(self, parent, index):
        node_to_split = parent.children[index]
        new_node = BTreeNode(is_leaf=node_to_split.is_leaf)

        parent.keys.insert(index, node_to_split.keys[2])
        parent.children.insert(index + 1, new_node)

        new_node.keys = node_to_split.keys[3:]
        node_to_split.keys = node_to_split.keys[:2]

        if not node_to_split.is_leaf:
            new_node.children = node_to_split.children[3:]
            node_to_split.children = node_to_split.children[:3]

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.is_leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if node.children[i].is_full():
                self._split(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def print_tree(self):
        self._print_node(self.root, 0)

    def _print_node(self, node, level):
        if node:
            print(f"Level {level}: {node.keys}")
            if not node.is_leaf:
                for child in node.children:
                    self._print_node(child, level + 1)


# Example usage:
if __name__ == "__main__":
    btree = BTree()
    keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    for key in keys:
        btree.insert(key)

    btree.print_tree()
