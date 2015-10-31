import Tree
from pprint import pprint

tree = {
    1: [2, 6, 9],
        2: [3, 4, 5],
            3: [],
            4: [],
            5: [],
        6: [7, 8],
            7: [],
            8: [],
        9: [10],
            10: []
}


agg_one = []
for t in Tree.aggs(tree):
    agg_one.append(t)