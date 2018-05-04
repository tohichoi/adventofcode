#/usr/bin/env python


# part1
def part1():
    s=0
    for line in fd.readlines():
        dim=map(lambda x : int(x), line.strip().split('x'))

        #print dim
        mindim=min(dim[0]*dim[1], dim[1]*dim[2], dim[2]*dim[0])
    
        s+=2*(dim[0]*dim[1]+dim[1]*dim[2]+dim[2]*dim[0])+mindim

    print s


# part1
def part2():
    s=0
    for line in fd.readlines():
        dim=map(lambda x : int(x), line.strip().split('x'))

        dim.sort()

        # print dim

        s0=2*(dim[0]+dim[1])+dim[0]*dim[1]*dim[2]
        # print s0
        
        s+=s0

    print s


fd=open('input.txt', 'r')

part2()

fd.close()
