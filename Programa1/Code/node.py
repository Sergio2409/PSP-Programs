# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    @property
    def has_next(self):
        '''Return True if the node has a next otherwise returns False.

        '''
        return True if self.next else False

    def __repr__(self):
        return str(self.value)
