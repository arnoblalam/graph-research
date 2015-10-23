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
    temp = copy(tree)
    children_1 = filter(lambda x: x != node_ids[1], temp[node_ids[0]])
    children_2 = filter(lambda x: x != node_ids[0], temp[node_ids[1]])
    merged_children = children_1 + children_2
    temp.pop(node_ids[0], None)
    temp.pop(node_ids[1], None)
    temp[node_ids] = merged_children
    return temp

def possible_aggs(merge_list):
    results = []
    for x in merge_list:
        for y in x:
            [results.append(z) for z in y if type(z) is tuple]
    return results

tree = {
    1: [2, 6, 9],
        2: [3, 4, 5],
            3: [],
            4: [],
            5: [],
        6: [7, 8],
            7: [],
            8: [],
        9: []
}

def aggs(ps, tree):
    results = []
    for p in ps:
        results.append(merge_nodes(p, tree))
        print results
    return results

print "Original Tree"
pprint(tree, width=25)

pprint(walk(tree))

print "Merged tree"
pprint(merge_nodes((1,2), tree), width=30)
