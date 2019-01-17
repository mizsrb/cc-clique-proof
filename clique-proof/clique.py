#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ULL - Complejidad Computacional 2018/2019
#
# CLIQUE class

class Clique:
    def __init__(self, g, k):
        # Initialize CLIQUE problem with graph and positive integer
        self.graph = g
        self.k = 0
        if k >= 0:
            self.k = k
