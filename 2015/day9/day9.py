#!/usr/bin/env python


import StringIO
import networkx as nx
import matplotlib.pyplot as plt
# from networkx.drawing.nx_pydot import write_dot
import pygraphviz

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

    G.add_edge(tokens[0], tokens[2], label=int(tokens[4]))

# print G['London']['Belfast']['label']

# using plt
# nx.draw(G, with_labels = True)
# plt.show()

# using graphviz
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
edge_labels = nx.get_edge_attributes(G, 'label')
# edge_labels = { (u,v): d['label'] for u,v,d in G.edges(data=True) }

print edge_labels
nx.draw(G, pos=pos)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
nx.drawing.nx_agraph.write_dot(G, 'file.dot')


# for every path
dist = {}
nodes = list(G.nodes())
for n in nodes:
    print n
    for path in nx.all_simple_paths(G, source=n, target=n, cutoff=len(G)):
        print path
        # for n in list(G.nodes()):
            # dist[n]+=G[n][n]['label']

for k, v in dist.items():
    print k, v

# fd.close()

