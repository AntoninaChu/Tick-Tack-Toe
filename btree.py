from btnode import BTNode

class BinaryTree:
    '''This class presents a binary tree.'''

    def __init__(self):
        '''This function sets a root of tree to None and creates object of class.'''
        self._root = None

    def add_root(self, item):
        '''This function receives an item and adds a root to tree with that item.'''
        self._root = BTNode(item)
        return self._root

    def find(self, item):
        '''This function receives an item and looks for it in tree.'''
        assert self._root != None, 'ValueError'
        def recurse(node):
            if node != None:
                if node.data == item:
                    return True
                recurse(node.left)
                recurse(node.right)
        return recurse(self._root) == True

    def add_left(self, node, item):
        '''This function takes node of tree and add left child to it.'''
        return node.set_left(item)

    def add_right(self, node, item):
        '''This function takes node of tree and adds right child to it.'''
        return node.set_right(item)