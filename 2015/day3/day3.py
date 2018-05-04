#!/usr/bin/env python


from collections import defaultdict


# initial position
def part1(data, H, ix, iy):

    cx=ix
    cy=iy

    for s in data:
        dx=0
        dy=0
        if s == '^':
            dy=1
        elif s == 'v':
            dy=-1
        elif s == '<':
            dx=-1
        elif s == '>':
            dx=1
        else:
            print 'Invalid direction: ' + s
            break

        cx+=dx
        cy+=dy
        
        H[(cx, cy)]+=1

    return H.keys()


def part2(data, H, ix, iy):

    data_santa=[data[i] for i in range(0, len(data), 2)]
    data_robot=[data[i] for i in range(1, len(data), 2)]

    part1(data_santa, H, ix, iy)
    part1(data_robot, H, ix, iy)

    
fd=open('input.txt')

data=fd.read().strip()
#data='^v^v^v^v^v'


H=defaultdict(int)
H[(0, 0)]=1

# part1(data, H, 0, 0)

part2(data, H, 0, 0)

print len(H.keys())

fd.close()

