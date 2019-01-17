#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ULL - Complejidad Computacional 2018/2019
#
# Main file with transformation from 3-SAT to CLIQUE

import matplotlib.pyplot as plt
import networkx as nx
from clique import *
from three_sat import ThreeSat

def transform3SAT2CLIQUE(sat):
    G = nx.Graph()
    k = len(sat.clauses)

    for clause in range(len(sat.clauses)):
        for literal in sat.clauses[clause].literals:
            node = "C" + str(clause) + "-" + literal.name
            G.add_node(node, clause=clause, name=literal.name, value=literal.value)

    for i in G.nodes(data=True):
        for j in G.nodes(data=True):
            if i[1]["clause"] != j[1]["clause"]:
                if i[1]["name"] != j[1]["name"] or i[1]["value"] != j[1]["value"]:
                    G.add_edge(i[0], j[0])

    nx.draw(G, with_labels=True, node_color='skyblue')
    plt.show()

    clique = Clique(G, k)
    return clique

#####################################################

print("Proof that CLIQUE is NP-complete")

sat = ThreeSat("data/ejemplo.txt")
clique = transform3SAT2CLIQUE(sat)
