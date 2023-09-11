fhand=open(input("Podaj nazwę pliku"))
file=dict()
for line in fhand:
    if not line.startswith("From "):continue
    line=line.split()
    mail=line[1]
    if mail not in file:
        file[mail]=1
    else:
        file[mail]+=1
print(file)
#newFile=list()
#for key, val in list(file.items()):
    #newFile.append((val,key))
newFile=[(val,key) for key,val in file.items()]
print(newFile)
newFile.sort(reverse=True)
for key, val in newFile[:1]:
    print(key,val)