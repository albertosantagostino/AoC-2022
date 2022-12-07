#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class FSNode
"""

from enum import Enum


class FSMode(Enum):
    DIR = 0
    FILE = 1


class FSNode():
    """A filesystem node (like an Unix inode)"""
    def __init__(self, name, mode: FSMode, size=None, parent=None, children=None):
        self.name = name
        self.mode = mode
        self.size = size or 0
        self.parent = parent
        self.children = children or []

    def __repr__(self):
        return f"FSNode('{self.name} ({self.mode})')"

    def add_child(self, name, mode):
        child = FSNode(name=name, mode=mode, parent=self)
        self.children.append(child)
        return child

    def isdir(self):
        return self.mode == FSMode.DIR

    def isfile(self):
        return self.mode == FSMode.FILE


def populate_dir_size(node):
    """Populate directories size, looking at all children recursively"""
    # TODO: Make this function callable multiple times without accumulating the sizes
    # Possible solution: clear all the directories sizes before computing them again
    if node.isdir():
        for child in node.children:
            if child.mode == FSMode.DIR:
                node.size += int(populate_dir_size(child))
            else:
                node.size += int(child.size)
        return node.size
    else:
        return node.size


def traverse_tree(node):
    """Traverse the tree (inorder)"""
    yield node
    if node.children:
        for child in node.children:
            yield from traverse_tree(child)
    else:
        return


def print_tree(node, level=0):
    """Print the tree visualizing the hierarchy"""
    info += f"{node.name} ({node.size})"
    print(f"{(info):>{level*15}}")
    if node.children:
        for child in node.children:
            print_tree(child, level + 1)
    else:
        return
