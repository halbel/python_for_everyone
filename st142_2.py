fhand=open(input("Podaj nazwę pliku"))
file=dict()
for line in fhand:
    if not line.startswith("From ") :continue
    line=line.split()
    words=line[2]
    if words not in file:
        file[words]=1
    else:
        file[words]+=1


print(file)

