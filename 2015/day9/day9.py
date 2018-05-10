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

# fd=StringIO.StringIO(s)
fd=open('input.txt')
    
G=nx.Graph()

for line in fd.readlines():
    tokens=line.strip().split()
    if len(tokens) < 5:
        continue
    
    G.add_edge(tokens[0], tokens[2], weight=int(tokens[4]))

res=dict(Dijkstra(G))

nx.draw(G, with_labels = True)
plt.show()
# nx.draw_graphviz(G)

fd.close()
