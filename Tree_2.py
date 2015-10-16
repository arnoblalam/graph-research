from toposort import toposort
from itertools import permutations

from itertools import tee, izip

def pairwise(iterable):
    """From
    http://stackoverflow.com/questions/5764782/iterate-through-pairs-of-items-in-a-python-list"""
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)
    
def agg(tree, f):
    """FInd all the aggregations/summaries of a tree"""
    raise NotImplementedError("Not yet implemented")
    
def traverse(tree):
    """Return the order in which the tree should be walked"""
    return list(toposort(tree))

def permute(path):
    """Given a set representing a path, finds all permutations of it"""
    return list(permutations(path))

def permute_traversal_list(ps):
    """Given a list of paths, finds the permutations of each sublist"""
    return [permute(path) for path in ps]

    #        1
    #       / \ \
    #      /   \ \ 
    #     /     \ 9
    #    /       \
    #   2         6
    #  /\ \      / \
    # /  \ \    /   \
    #3    4 5  7     8

tree = {
    1: {2, 6, 9},
    2: {3, 4, 5},
    6: {7, 8}
}

tree_nodes = {1: 50.0, 2: 25.0, 3: 12.5, 4: 26.0, 5: 27, 6: 75, 7: 74, 8: 76, 9: 1100}

x = list(toposort(tree))

print(x)

paths = []
for x in x:
    paths.append(list(permutations(x)))

aggregate = []
for subpaths in paths:
    subpath_aggregate= []
    for permutation in subpaths:
        sub_results = []
        if len(permutation) == 1:
            sub_results.append(tree_nodes[permutation[0]])
        for (x, y) in pairwise(permutation):
            sub_results.append(tree_nodes[x] - tree_nodes[y])
        subpath_aggregate.append(sub_results)
    aggregate.append(subpath_aggregate)
        