try:    
    number = float(input("podaj liczbe pomiedzy 0.0 a 1.0"))
    if number >=0.0 and number <=1.0:
        if number >=0.9:
            print("5,0")
        elif number >=0.8:
            print("4,5")
        elif number >=0.7:
            print("4,0")
        elif number >=0.6:
            print("3,5")
        elif number >=0.5:
            print("3,0")
        elif number < 0.5:
            print("2,0")
    else:
        print("bład, niepoprawna wartosc")
except:
    print("niepoprawne dane")        

def computergrade(a):
    if a>=0.9:
        print("5,0")
    
computergrade(number)