#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Arnob L. Alam'
__copyright__ = 'Copyright 2015, Arnob L. Alam'
__license__ = 'GPL v3'

from itertools import permutations
from copy import copy
from pprint import pprint


def permute(xs):
    """Given a list of xs, returns a list of the permuations of xs
    permute :: [a] --> [(a)]
    """
    return list(permutations(xs))

def add_to_head_of_perm(y, ys):
    """Given a list, adds item to head of list.
    add_to_head_of_perm :: a --> [a] --> [a]
    """
    return tuple([y] + list(ys))

def pairwise(ys):
    """Given a sequence, returns a list of lists, obtained by tupling up items. Example
    (1, 2, 3) -> [[(1, 2), 3], [1, (2, 3)]]
    pairwise :: [a] --> [[a_]]
    """
    seq_length = len(ys)
    results = []
    for k, v in enumerate(ys):
        if k+1 == seq_length:
            break
        first = list(ys[0:k])
        pair = (ys[k], ys[k+1])
        rest = list(ys[k+2:])
        temp = first + [pair] + rest
        results.append(temp)
    return results

def walk(tree):
    """Given a tree, generates all possible aggregations
    walk :: (Dict a) => a -> [a_]
    """
    results = []
    for parent, children in tree.iteritems():
        perms = permute(children)
        temp = copy(perms)
        # Add the parent to the perms as well
        for perm in temp:
            perms.append(add_to_head_of_perm(parent, perm))
        for perm in perms:
            results.append(pairwise(perm))
    return results

def merge_nodes(node_ids, tree):
    """Merges nodes in a tree together
    merge_nodes :: (Dict b) => (a, a) -> b -> b
    """
    # Don't merge nodes if they are already merged
    if node_ids in tree or tuple(reversed(node_ids)) in tree:
        return tree
    # Copy the tree so we keep the original intact
    temp = copy(tree)
    # Get all the children of each node (except if that child is the one being merged)
    children_1 = filter(lambda x: x != node_ids[1], temp[node_ids[0]])
    children_2 = filter(lambda x: x != node_ids[0], temp[node_ids[1]])
    merged_children = children_1 + children_2
    # Remove the original nodes in the tree
    temp.pop(node_ids[0], None)
    temp.pop(node_ids[1], None)
    # Add a new node
    temp[node_ids] = merged_children
    # Replace references to the old node in the parent with references to the new node
    #parent = find_parent(node_ids[0], temp)
    #if parent:
    #    try:
    #        pos = temp[parent].index(node_ids[0])
    #        temp[parent].remove(node_ids[0])
    #        temp[parent].remove(node_ids[1])
    #        temp[parent].insert(pos, node_ids)
    #    except ValueError:
    #        print temp[parent]
    #        print node_ids
    #        raise
    return temp
    
def find_parent(node_id, tree):
    for k, v in tree.iteritems():
        if node_id in v:
            return k
        else:
            continue

def possible_aggs(merge_list):
    """Generates possible aggregations of a tree"""
    results = []
    for x in merge_list:
        for y in x:
            [results.append(z) for z in y if type(z) is tuple]
    return results

def aggs(tree):
    """Given a list of possible aggregations, generates possible trees"""
    ps = possible_aggs(walk(tree))
    results = []
    for p in ps:
        results.append(merge_nodes(p, tree))
    return results