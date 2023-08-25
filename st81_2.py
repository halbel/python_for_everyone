numlist=list()
while True:
    line = input("podaj liczbę: ")
    if line == 'gotowe':break
    try:
        value=float(line)
        numlist.append(line)
        x=min(numlist)
        y=max(numlist)
    except:
        print('piszesz bzdury')
print(x,y)