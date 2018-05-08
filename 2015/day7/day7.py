#!/usr/bin/env python


# refer : https://bitbucket.org/JIghtuse/adventofcode/src/0aa3b58dfa221bc7f5dca4628b783d544a54688d/day7/python/part_one.py?at=master&fileviewer=file-view-default

from collections import defaultdict
import numpy as np
import StringIO

def lookup_cache(f):
    cache={}
    def func(graph, key, depth):
        if key not in cache:
            cache[key] = f(graph, key, depth)
        return cache[key]
    return func


# v: symbol
# d: depth
@lookup_cache
def eval_statement(T, v, d):

    try:
        num=int(v)
        # print 'Terminal : ' + v
        return num
    except ValueError:
        pass

    print '%s%s = %s' % (' '*d, v, T[v])
    
    s=T[v]
    n=len(s)

    # print s
    
    if n==1:
        return eval_statement(T, s[0], d+1)
    elif n==2:
        if s[0]=='NOT':
            return np.invert(eval_statement(T, s[1], d+1))
        else:
            raise Exception('Invalid OP : ' + s[0])
    elif n==3:
        a=eval_statement(T, s[0], d+1)
        b=eval_statement(T, s[2], d+1)
        r=None
        
        if s[1]=='AND':
            r=np.bitwise_and(a, b)
            # print '%s ==> %d %s %d' % (' '.join(s), a, s[1], b)
        elif s[1]=='OR':
            r=np.bitwise_or(a, b)
            # print '%s ==> %d %s %d' % (' '.join(s), a, s[1], b)
        elif s[1]=='LSHIFT':
            r=np.left_shift(a, b)
            # print '%s ==> %d %s %d' % (' '.join(s), a, s[1], b)
        elif s[1]=='RSHIFT':
            r=np.right_shift(a, b)
            # print '%s ==> %d %s %d' % (' '.join(s), a, s[1], b)
        else:
            raise Exception('Invalid OP : ' + s[1])
        return r

    raise Exception('Invalid statement : ' + ' '.join(s))
    return None
    
# T : key:symbol, value: [ OP|CONSTANT, a, [b] ]
T=defaultdict(list)

instructions='''123 -> x
x AND y -> d
y RSHIFT 2 -> g
x OR y -> e
NOT x -> h
456 -> y
x LSHIFT 2 -> f
NOT y -> i'''

fd=open('input.txt')
# fd=StringIO.StringIO(instructions)

# build table
for line in fd.readlines():
    tokens=line.strip().split()
    
    n=len(tokens)

    T[tokens[-1]]=tokens[0:-2]

# for k, v in T.items():
    # print '%s = %s' % (k, v)

# part2
# Now, take the signal you got on wire a,
# override wire b to that signal, and reset the other wires (including wire a).
# What new signal is ultimately provided to wire a?

T['b']=['3176']
    
res=eval_statement(T, 'a', 0)
print res & 0xffff

fd.close()
