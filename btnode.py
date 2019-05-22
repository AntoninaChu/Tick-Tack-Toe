class BTNode:
    '''THis class presents a node for binary tree.'''

    def __init__(self, data, parent=None):
        '''This function receives data and creates a node with that data. Parent is set to None by default.'''
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def set_left(self, item):
        '''This function receives an item and adds it to left child of self.'''
        assert self.left == None, 'This position already exist.'
        self.left = BTNode(item, self)
        return self.left

    def set_right(self, item):
        '''This function receives an item and adds it to right child of self.'''
        assert self.right == None, 'This position already exist'
        self.right = BTNode(item, self)
        return self.right