import Tree

artificial_tree = {
1:[2,3,4],
2:[5,6],
3:[7,8,9],
4:[10,11,12,13],
5:[14,15,16,17],
6:[18,19],
7:[20,21,22,23,24],
8:[],
9:[],
10:[25,26,27],
11:[],
12:[28,29,30],
13:[],
14:[],
15:[],
16:[],
17:[],
18:[],
19:[],
20:[],
21:[],
22:[],
23:[],
24:[],
25:[],
26:[],
27:[],
28:[],
29:[],
30:[],
}

artificial_tree_weights ={
1: 100,
2: 20,
3: 50,
4: 80,
5: 10,
6: 30,
7: 20,
8: 40,
9: 400,
10:50,
11:30,
12:80,
13:60,
14:20,
15:30,
16:150,
17:80,
18:40,
19:200,
20:10,
21:130,
22:50,
23:80,
24:60,
25:70,
26:260,
27:30,
28:40,
29:10,
30:20,
}

reduced_artificial_trees = Tree.agg_to(artificial_tree, 9)

agg_weights = [Tree.apply_aggregation(t, artificial_tree_weights) for t in reduced_artificial_trees]
H = [Tree.calculate_H(x) for x in agg_weights]
S = [Tree.calculate_S(x) for x in agg_weights]
Tree.aggregate(artificial_tree,artificial_tree_weights, 9, keep_intermediate=True, order_matters=False)
