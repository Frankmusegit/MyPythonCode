#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import *
from Element import *

class BspTreeVisitor:
    pass

class InsertItemBspTreeVisitor(BspTreeVisitor):

    def __init__(self):
         self.item =  Element()
    def visit(self, items = list()):
         items.append(self.item)

class RemoveItemBspTreeVisitor(BspTreeVisitor):

    def __init__(self):
         self.item =  Element()

    def visit(self, items = list()):
         items.remove(self.item)

class FindItemBspTreeVisitor(BspTreeVisitor):

    def __init__(self):
         self.foundItems = list()

    def visit(self, items = list()):
        for i in range(0, len(items)):
            item = items[i]
            if not item.itemDiscovered:
                item.itemDiscovered = 1
                self.foundItems.append(item)

class Node:
    def __init__(self):
        self.offset = 0
        self.leafIndex = 0
        self.type = 0

class BspTree:
    def __init__(self, a = 0):
        self.leafCnt = a
        self.insertVisitor = InsertItemBspTreeVisitor()
        self.removeVisitor = RemoveItemBspTreeVisitor()
        self.findVisitor = FindItemBspTreeVisitor()
        self.depth = 0
        self.rect = 0
        self.nodes = [Node()]
        self.leaves = list()

    def intmaxlog(self, n):
        if n > 0:
            return qMax(int(ceil(log(n)/log(2))), 5)
        else:
            return 0

    def initialize(self, rect, n):
        self.depth      = self.intmaxlog(n)
        self.rect = rect
        self.leafCnt    = 0
        for i in range(0, (1 << (self.depth+1)) - 1):
            self.nodes.append(0)
        for i in range(0, (1 << self.depth)):
            self.leaves.append(0)
        self.initialize2(rect, self.depth, 0)

    def initialize2(self, rect, depth, index):
        node = self.nodes[index]
        if index == 0:
            node.type = Type.Horizontal
            node.offset = rect.center().x()
        if depth:
            type = Type()
            rect1 = QRectF()
            rect2 = QRectF()
            offset1 = 0
            offset2 = 0
            if node.type == Type.Horizontal:
                type = Type.Vertical
                rect1.setRect(rect.left(), rect.top(), rect.width(), rect.height() * .5)
                rect2.setRect(rect1.left(), rect1.bottom(), rect1.width(), rect.height() - rect1.height())
                offset1 = rect1.center().x()
                offset2 = rect2.center().x()
            else:
                type = Type.Horizontal
                rect1.setRect(rect.left(), rect.top(), rect.width() * .5, rect.height())
                rect2.setRect(rect1.right(), rect1.top(), rect.width() - rect1.width(), rect1.height())
                offset1 = rect1.center().y()
                offset2 = rect2.center().y()

            childIndex = self.firstChildIndex(index)
            child   = self.nodes[childIndex]
            child.offset = offset1
            child.type   = type

            child = self.nodes[childIndex + 1]
            child.offset = offset2
            child.type   = type

            self.initialize(rect1, depth - 1, childIndex)
            self.initialize(rect2, depth - 1, childIndex + 1)
        else:
            node.type      = Type.Leaf
            node.leafIndex = self.leafCnt + 1