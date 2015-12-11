import Tree

print("Loading the tree")
test_tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7, 8, 9],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
    }
    
 
node_weights = {
    1: 100,
    2: 50,
    3: 80,
    4: 20,
    5: 50,
    6: 30,
    7: 50,
    8: 100,
    9: 200
    }
    
Tree.aggregate(test_tree, node_weights, 6, keep_intermediate=True)
#aggregated_trees = Tree.agg_to(test_tree, node_weights, 6, keep_intermediate=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
#print "Done"
#
#print "Reducing the tree to 6 nodes"
#    
#reduced_trees = Tree.agg_to(test_tree, 6)
#
#print "Done"
#
#print "Checking if lower left example tree from figure 2 in paper is in the permutations"
#
#check_tree = {
#    1: [(2, (4, 5)), 3],
#    (2, (4, 5)): [],
#    3: [(6, 7), 8, 9],
#    (6, 7): [],
#    8: [],
#    9: []
#    }
#
#print check_tree in reduced_trees
#
#print "Checking if lower right example tree from figure 2 in paper is in the permutations"
#
#check_tree_2 = {
#    1: [2, 3],
#    2: [(4, 5)],
#    3: [6, ((7, 8), 9)],
#    (4, 5): [],
#    6: [],
#    ((7, 8), 9): []
#    }
#print check_tree_2 in reduced_trees
#
#print "Calculating the entropy for the set of reduced trees"
#
#agg_weights = [Tree.apply_aggregation(t, node_weights) for t in reduced_trees]
#
#H = [Tree.calculate_H(x) for x in agg_weights]
#S = [Tree.calculate_S(x) for x in agg_weights]