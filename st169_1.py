import re
fhand=open("mbox.txt")
xhand=input("enter your key:")
w=0
for line in fhand:
    x=line.lstrip()
    f=re.search(xhand,x)
    if f:
        w+=1
    else: continue
    

print(w)
