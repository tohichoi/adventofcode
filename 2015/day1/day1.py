#!/usr/bin/env python

import StringIO

'''

  ( : +1
  ) : -1

'''

def part2(data2):
    s=0
    target_val=-1
    for i in range(len(data2)):
        s=s+data2[i]
        if s==target_val:
            print i+1
            break

       
def part1(data):
    # 읽을 때 strip()을 하지 않으면 else 문에서 \n을 -1로 한 번 더 센다
    data2=map(lambda x : 1 if '(' in x else -1, data)

    print sum(data2)

    part2(data2)
    

with open('data.txt', 'r') as myfile:
  data = myfile.read().strip()

  part1(data)

