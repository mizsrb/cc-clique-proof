#! /usr/bin/env python
# -- coding: utf-8 --

# ULL - Complejidad Computacional 2018/2019
#
# 3-SAT class and its auxiliary classes

class Literal:
    def __init__(self, literal_string):
        self.name = literal_string
        self.value = True
        if literal_string[0] == '~':
            self.value = False
            self.name = literal_string[1:]

    def __repr__(self):
        if self.value:
            return self.name
        return "~" + self.name


class Clause:
    def __init__(self, clause_string):
        self.literals = []
        literals_repr = clause_string.split()
        for str in literals_repr:
            self.literals.append(Literal(str))

    def __repr__(self):
        return str(self.literals)


class ThreeSat:
    def __init__(self, problem_file):
        self.clauses = []
        self.read_from_file(problem_file)

    def read_from_file(self, file):
        f = open(file, 'r')
        clause_string = f.readline()
        while clause_string != "":
            self.clauses.append(Clause(clause_string))
            clause_string = f.readline()
        f.close()

    def __repr__(self):
        return str(self.clauses)
