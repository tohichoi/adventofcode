#!/usr/bin/env python


import re
import StringIO


def parse_code2(s):

    i=0
    rs=''
    ns=len(s)
    
    while i < ns:
       
        if s[i]=='"':
            # begin
            if i==0:
                i+=1
                rs+='"\\"'
                continue
            # end
            if i==ns-1:
                rs+='\\""'
                print rs
                return (rs, len(rs))
        elif s[i]=='\\':
            if s[i+1]=='"' or s[i+1]=='\\':
                rs+='\\\\'
                rs+='\\'+s[i+1]
                i+=2
            elif s[i+1]=='x':
                rs+='\\\\'+s[i+1:i+4]
                i+=4
            else:
                rs+='\\\\'
                i+=1
        else:
            rs+=s[i]
            i+=1

    return (rs, len(rs))


def parse_code(s):

    i=0
    rs=''
    ns=len(s)
    
    while i < ns:
        if s[i]=='"':
            # begin
            if i==0:
                i+=1
                continue
            # end
            if i==ns-1:
                return (rs, len(rs))
        elif s[i]=='\\':
            if s[i+1]=='"' or s[i+1]=='\\':
                rs+=s[i+1]
                i+=2
            elif s[i+1]=='x':
                rs+=chr(int(s[i+2:i+4], 16))
                i+=4
            else:
                i+=1
                rs+=s[i]
        else:
            rs+=s[i]
            i+=1
            
    return (rs, len(rs))

s=r'''
""
"abc"
"aaa\"aaa"
"\x27"
'''

# s=r'''
# "aaa\"aaa"
# "\x27"
# '''

# fd=StringIO.StringIO(s)
fd=open('input.txt')

ncode=0
nstr=0
for line in fd.readlines():

    p=line.strip()
    if len(p) < 1:
        continue
    ncode+=len(p)

    # part1
    # (rs, i)=parse_code(p)

    # part2
    (rs, i)=parse_code2(p)
    
    nstr+=i

# part1
# print ncode-nstr

# part2
print nstr-ncode


fd.close()
