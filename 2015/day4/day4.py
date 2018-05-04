#/usr/bin/env python


import md5

s='yzbqklnj'

for i in range(9999999):
    m=md5.new()

    s2=s+str(i)
    
    m.update(s2)

    res=m.hexdigest()

    if res[0:6] == '000000':
        print s2

