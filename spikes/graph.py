import networkx as nx
import matplotlib.pyplot as plt

nodes = [1, 2, 3]
edges = [(1, 2), (2, 3), (1, 3)]

G = nx.Graph()
#G.add_nodes_from(nodes)
G.add_edges_from(edges)

edges = G.edges()
for edge in edges:
    string = ""
    for x in edge:
        string += str(x) + ' '
    print(string)

cliques = list(nx.find_cliques(G))

for clique in cliques:
    print(clique)
    input()
    for node in clique:


nx.draw(G)
plt.show()
input()
