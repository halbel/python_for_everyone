import re
fhand=open("mbox.txt")
#
l=list()
w=0
for line in fhand:
    x=line.rstrip()
    f=re.findall("^New Revision: ([0-9]+)",x)
    if len(f)>0:
        l.append(f[0])
    else:continue
for x in l:
    x=int(x)
    w+=x
y=int(w/len(l))
print(y)
