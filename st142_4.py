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
dane=file.values()
biggest=0
for x in file.values():
    if x == 0 or x > biggest:
        biggest=x
print(mail, biggest)
