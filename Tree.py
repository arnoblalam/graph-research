# -*- coding: utf-8 -*-
from __future__ import division
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Arnob L. Alam'
__copyright__ = 'Copyright 2015, Arnob L. Alam'
__license__ = 'GPL v3'

from itertools import permutations
#from copy import deepcopy, copy
import cPickle
from pprint import pprint
from math import log
from csv import DictWriter

def deepcopy(obj):
    return cPickle.loads(cPickle.dumps(obj, -1))


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
        temp = deepcopy(perms)
        # Add the parent to the perms as well
        for perm in temp:
            perms.append(add_to_head_of_perm(parent, perm))
        for perm in perms:
            r = pairwise(perm)
            results.append(r)
    return results

def merge_nodes(node_ids, tree):
    """Merges nodes in a tree together
    merge_nodes :: (Dict b) => (a, a) -> b -> b
    """
    # Copy the tree so we keep the original intact
    temp = deepcopy(tree)
    # Don't merge nodes if they are already merged
    if node_ids in temp or tuple(reversed(node_ids)) in temp:
        return temp
    # Get all the children of each node we need to merge (except if that child is the other node)
    children_1 = filter(lambda x: x != node_ids[1], temp[node_ids[0]])
    children_2 = filter(lambda x: x != node_ids[0], temp[node_ids[1]])
    merged_children = children_1 + children_2
    # Remove the original nodes in the tree
    temp.pop(node_ids[0], None)
    temp.pop(node_ids[1], None)
    # Add a new node
    temp[node_ids] = merged_children
    
    # Update references to the old node with references to the new node
    for k, v in temp.iteritems():
        if node_ids[0] in v:
            idx = v.index(node_ids[0])
            v.remove(node_ids[0])
            v.insert(idx, node_ids)
        if node_ids[1] in v:
            idx = v.index(node_ids[1])
            v.remove(node_ids[1])
            v.insert(idx, node_ids)
        temp[k] = dedupe(v)
    return temp
    
def dedupe(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]
    

def possible_aggs(merge_list, restricted_nodes = []):
    """Generates possible aggregations of a tree"""
    results = set()
    for x in merge_list:
        for y in x:
            for k, z in enumerate(y):
                if type(z) is tuple:
                    results.add(z)
    results = filter(lambda x: x[0] not in restricted_nodes and x[1] not in restricted_nodes, results)
    for result in results:
        try:
            results.remove(tuple(reversed(result)))
        except ValueError:
            continue
    return list(results)

def aggs(tree, weights):
    """Given a list of possible aggregations, generates possible trees"""
    restricted_nodes =[]
    weights = apply_aggregation(tree, weights)
    for parent, children in tree.iteritems():
        children_weights = {}
        for child in children:
            children_weights[child] = weights[child]
        try:
            restricted_nodes.append(max(children_weights, key=children_weights.get))
        except ValueError:
            pass
    ps = possible_aggs(walk(tree), restricted_nodes)
    results = []
    for p in ps:
        e = merge_nodes(p, tree)
        if e not in results:
            results.append(e)
    return results
    
def agg_to(tree, weights, desired_level, keep_intermediate=False):
    """agg_to :: Tree a -> Int -> [Tree a]
    """
    current_level = len(tree)
    if desired_level < 2:
        raise Exception("Resulting tree must have at least two nodes")
    elif desired_level >= current_level:
        return [tree]
    else:
        n = len(tree) - desired_level
        results = []
        for i in range(1, n+1):
            r = reduce_n_times(tree, i, weights)
            [results.append(s) for s in r]
        if keep_intermediate == True:
            return results
        else:
            return filter(lambda x: len(x) == desired_level, results)
        
        
def reduce_n_times(tree, n, weights):
    """Reduce a tree n times. E.g. if you have a 4 node tree and you reduce it
    once, you get back all the 3 node trees.  If you reduce it twice, you get
    back all the 2 node trees"""
    k = []
    if n==1:
        aggs_ = aggs(tree, weights)
        agg_weights = [apply_aggregation(t, weights) for t in aggs_]
        H = [calculate_H(x) for x in agg_weights]
        sorted_H = [i[0] for i in sorted(enumerate(H), key=lambda x:x[1], reverse=True)][0:10]
        for i in sorted_H:
            k.append(aggs_[i])
        return k
    if n>1:
        trees = reduce_n_times(tree, n-1, weights)
        results = []
        for tree in trees:
            results = results + aggs(tree, weights)
        agg_weights = [apply_aggregation(t, weights) for t in results]
        S = [calculate_S(x) for x in agg_weights]
        sorted_S = [i[0] for i in sorted(enumerate(S), key=lambda x:x[1], reverse=True)][0:10]
        for i in sorted_S:
            k.append(results[i])
        return k
            
def apply_aggregation(t, node_data, f=lambda x, y: x+y):
    """Create the new tree t by applying the aggregations to weights described in node_data"""
    try:
        result = dict()
        for k, v in t.iteritems():
            if type(k) is not tuple:
                result[k] = node_data[k]
            else:
                result[k] = apply_tuple(k, node_data, f)
        return result
    except:
        print(t)
        raise
    
def apply_tuple(t, n, f):
    if type(t[0]) is not tuple and type(t[1]) is not tuple:
        return f(n[t[0]], n[t[1]])
    elif type(t[0]) is tuple and type(t[1]) is tuple:
        return f(apply_tuple(t[0], n, f), apply_tuple(t[1], n, f))
    elif type(t[0]) is tuple:
        return f(apply_tuple(t[0], n, f), n[t[1]])
    elif type(t[1]) is tuple:
        return f(n[t[0]], apply_tuple(t[1], n, f))
        
def calculate_H(n):
    total = sum(n.itervalues())
    weights =  [wi/total for wi in n.itervalues()]
    return -sum([wi*log(wi) for wi in weights])

def calculate_S(n):
    return calculate_H(n)/log(len(n))
    
def calculate_P(n):
    W = sum(n.itervalues())
    ws =  n.itervalues()
    return -sum([(wi/W)*log(wi/W, 2) for wi in ws])
    
def write_tree_ids(entropy_list, trees, fname):
    with open(fname, 'w') as csvfile:
        fieldnames = ["tree index", "length", "entropy"]
        writer = DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        for k, v in enumerate(entropy_list):
            w = {"tree index": k, "length": len(trees[k]), "entropy": v}
            writer.writerow(w)
    
def aggregate(tree, node_weights, desired_level, keep_intermediate=False):
    reduced_trees = agg_to(tree, node_weights, desired_level, keep_intermediate)
    agg_weights = [apply_aggregation(t, node_weights) for t in reduced_trees]
    H = [calculate_H(x) for x in agg_weights]
    S = [calculate_S(x) for x in agg_weights]
    sorted_H = [i[0] for i in sorted(enumerate(H), key=lambda x:x[1], reverse=True)]
    sorted_S = [i[0] for i in sorted(enumerate(S), key=lambda x:x[1], reverse=True)]
    write_tree_ids(H, reduced_trees, "absolute_entropies.csv")
    write_tree_ids(S, reduced_trees, "relative_entropies.csv")
    H_max = max(H)
    S_max = max(S)
    H_original=calculate_H(node_weights)
    
    print "The orignal tree had an entropy of {}".format(H_original)
    
    print "The reduced tree with the highest entropy had an entropy of {}".format(H_max)
    print "Here is a print out of that tree"
    pprint(reduced_trees[H.index(max(H))],width=25)
    print "And here are the associated weights for each node"
    pprint(agg_weights[H.index(max(H))],width=25)
    
    print "The reduced tree with the highest relative entropy had an entropy of {}".format(S_max)
    pprint(reduced_trees[S.index(max(S))],width=25)
    print "And here are the associated weights for each node"
    pprint(agg_weights[S.index(max(S))],width=25)
        
    print "Here are the IDs of the top 10 trees by Maximum Entropy"
    pprint(sorted_H[0:10])
    print "Here are the IDs of the top 10 trees by Reative Maximum Entropy"
    pprint(sorted_S[0:10])
