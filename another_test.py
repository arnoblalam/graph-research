import Tree 
artificial_tree = {
1:[2,3],
2:[4,5,6],
3:[7,8,13],
4:[],
5:[],
6:[9,10],
7:[],
8:[11,12,13,14,15],
9:[],
10:[],
11:[],
12:[],
13:[],
14:[],
15:[],
}

artificial_tree_weights ={
1: 100,
2: 20,
3: 80,
4: 80,
5: 320,
6: 30,
7: 20,
8: 40,
9: 400,
10:50,
11:30,
12:80,
13:180,
14:20,
15:75
}

Tree.aggregate(artificial_tree, artificial_tree_weights, 6, keep_intermediate=True)