import Tree

artificial_tree = {
1:[2,3,4],
2:[5,6],
3:[7,9],
4:[10,11,12,13],
5:[14,16,17],
6:[18,19],
7:[20,21,23,24],
9:[],
10:[26,27],
11:[],
12:[28,29],
13:[],
14:[],
16:[],
17:[],
18:[],
19:[],
20:[],
21:[],
23:[],
24:[],
26:[],
27:[],
28:[],
29:[]
}

artificial_tree_weights ={
1: 100,
2: 20,
3: 50,
4: 80,
5: 10,
6: 30,
7: 20,
9: 400,
10:50,
11:30,
12:80,
13:60,
14:20,
16:150,
17:80,
18:40,
19:200,
20:10,
21:130,
23:80,
24:60,
26:260,
27:30,
28:40,
29:10
}

Tree.aggregate(artificial_tree, artificial_tree_weights, 8, keep_intermediate=False)

aggregated_trees = Tree.agg_to(artificial_tree, artificial_tree_weights, 8, keep_intermediate=False)