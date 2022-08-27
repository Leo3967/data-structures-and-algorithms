# -*- coding: UTF-8 -*-
from pythonds.graphs import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # 建桶
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[i]