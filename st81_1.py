total=0
count=0
while True:
    line = input("podaj liczbę: ")
    if line == 'gotowe':break
    try:
        value=float(line)
        total=total+value
        count=count+1
    except:
        print("bzdury napisałeś")
average=total/count
print(total ,count ,average )    





