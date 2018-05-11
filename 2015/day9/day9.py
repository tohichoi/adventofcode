#!/usr/bin/env python


import StringIO
import networkx as nx
import matplotlib.pyplot as plt


def Dijkstra(G):

    return nx.all_pairs_dijkstra_path(G)


s='''
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
'''

fd=StringIO.StringIO(s)
# fd=open('input.txt')
    
G=nx.Graph()


# read graph
for line in fd.readlines():
    tokens=line.strip().split()
    if len(tokens) < 5:
        continue
    
    G.add_edge(tokens[0], tokens[2], weight=int(tokens[4]))

print G['London']['Belfast']['weight']

nx.draw(G, with_labels = True)
plt.show()
fd.close()

# for every path
for path in nx.all_simple_paths(G):
    dist={}
    for n in list(G.nodes()):
        G[n][n]['weight']
        dist[n]=
