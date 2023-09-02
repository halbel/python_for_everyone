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