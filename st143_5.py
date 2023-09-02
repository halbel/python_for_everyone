fhand=open(input("Poda nazwę pliku:"))
domains=dict()
for line in fhand:
    if not line.startswith("From "): continue
    line=line.split()
    mail=line[1]
    dom=mail.split("@",1)
    dom2=dom[1]
    if dom2 not in domains:
        domains[dom2]=1
    else:
        domains[dom2]+=1
print(domains)