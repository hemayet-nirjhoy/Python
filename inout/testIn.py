from collections import defaultdict

nb_edges = int(input())

g = defaultdict(dict)

for _ in range(nb_edges):
	u,v,weight = input().split()
	g[u][v] = int(weight)
	#g[u][v] = int(weight) for in undirected graph

print(g)

# python testIn.py < test.in > test.out 
