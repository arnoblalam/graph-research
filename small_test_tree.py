import Tree
from pprint import pprint


test_tree = {
    1: [2, 3, 4],
    2: [],
    3: [],
    4: []
    }
    
node_weights = {
    1: 50,
    2: 10,
    3: 60,
    4: 5
    }

reduced_trees = Tree.agg_to(test_tree, 2)

agg_weights = [Tree.apply_aggregation(t, node_weights) for t in reduced_trees]
H = [Tree.calculate_H(x) for x in agg_weights]
S = [Tree.calculate_S(x) for x in agg_weights]
Tree.aggregate(test_tree,node_weights, 2, keep_intermediate=True, order_matters=False)
