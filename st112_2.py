try:
    file=input("podaj nazwe pliku:")
    fhand=open(file)
    count=0
    y=0
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            x= line.find(" ")
            inp= line[x:]
            f=float(inp)
            y=f+y
            count=count+1
        
    print("srednia wartosc pewnosci spamu:", y/count)
except:
    if file.endswith(".txt"):
        print('Nie mo ż na otworzy ć pliku:',file)
    else:
        print(file.upper(),"-co za bzdury")