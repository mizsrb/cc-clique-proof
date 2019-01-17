#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ULL - Complejidad Computacional 2018/2019
#
# Main file with transformation from 3-SAT to CLIQUE

import networkx as nx

def transform3SAT2CLIQUE(sat):
    G = nx.Graph()

    # for x in range(sat.clauses):
        # for y in range(x.variables):
            # G.add_node(Cx-Vy)

    # for i in G.nodes:
        # for j in G.nodes:
            # if i.clause != j.clause:
                # if i.var != j.var or i.value != j.value
                    # G.add_edge(i, j)

    clique = new Clique(G, k)
    return clique

print("Proof that CLIQUE is NP-complete")
