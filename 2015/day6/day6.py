#!/usr/bin/env python


from collections import defaultdict

def count_lit(G):
    count=0
    for k in G.keys():
        count+=G[k]

    print count
    
    return count
    
def turn_on(G, x, y):
    G[(x, y)]=1

def turn_off(G, x, y):
    G[(x, y)]=0

def toggle(G, x, y):
    if G[(x, y)]==1:
        G[(x, y)]=0
    else:
        G[(x, y)]=1

def turn_on2(G, x, y):
    G[(x, y)]+=1

def turn_off2(G, x, y):
    G[(x, y)]=max(G[(x, y)]-1, 0)

def toggle2(G, x, y):
    G[(x, y)]+=2
    
def set_val(G, sx, sy, ex, ey, func):
    for y in range(sy, ey+1, 1):
        for x in range(sx, ex+1, 1):
            func(G, x, y)
            
G=defaultdict(int)

fd=open('input.txt')

for line in fd.readlines():

    tokens=line.strip().split()

    sidx=0
    eidx=0
    func=None
    if tokens[0]=='turn' and tokens[1]=='on':
        sidx=2
        eidx=4
        # func=turn_on
        func=turn_on2
    elif tokens[0]=='turn' and tokens[1]=='off':
        sidx=2
        eidx=4
        # func=turn_off
        func=turn_off2
    elif tokens[0]=='toggle':
        sidx=1
        eidx=3
        # func=toggle
        func=toggle2
    else:
        print 'Unknown instruction: ' + line

    p1=map(lambda x : int(x), tokens[sidx].split(','))
    p2=map(lambda x : int(x), tokens[eidx].split(','))

    # part1
    set_val(G, p1[0], p1[1], p2[0], p2[1], func)

    # print p1, p2, func, count_lit(G)
    print p1, p2, func
    
count_lit(G)
