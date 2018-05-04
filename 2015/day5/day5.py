#/usr/bin/env python


def is_nice(s):

    print 'input: %s' % s
    
    res=[0, 0, 0]
    
    # cond 1
    res[0]=0
    tmps=0
    for c in s:
        if c in 'aeiou':
            tmps+=1
    if tmps >= 3:
        # print 'True: ' + str(s3)
        res[0]=1

    # cond2
    res[1]=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            # print 'True: %c%c' % (s[i], s[i+1])
            res[1]=1
            break

    # cond3
    res[2]=1
    # ab, cd, pq, xy
    h={'ab':0, 'cd':0, 'pq':0, 'xy':0}
    for i in range(len(s)-1):
        if h.has_key(s[i]+s[i+1]):
            # print 'False: %c%c' % (s[i], s[i+1])
            res[2]=0
            break

    print res
            
    if sum(res)==3:
        return 1

    return 0


def is_nice2(s):

    print 'input: %s' % s
    
    res=[0, 0]

    for i in range(len(s)-1):
        cp=s[i]+s[i+1]
        for j in range(i+2, len(s)-1):
            if cp == s[j]+s[j+1]:
                res[0]=1
                break

    for i in range(len(s)-2):
        if s[i]==s[i+2]:
            res[1]=1
            break

    print res
    
    if sum(res)==2:
        return 1

    return 0


count=0

# part1 test
# data=['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
# for s in data:
    # count+=is_nice(s)

# part2 test
# [qj, zxz], [xx, xyz], [tg, 0], [0, odo]
# data=['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
# for s in data:
    # count+=is_nice2(s)

fd=open('input.txt')

for line in fd.readlines():
    s=line.strip()
    count+=is_nice2(s)

print count
