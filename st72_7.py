try:
    number = float(input("podaj liczbe pomiedzy 0.0 a 1.0"))

    def computergrade(a):
        if a >=0.0 and a<=1.0:
            if a>=0.9:
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
            print("niepoprawna wartość") 

    computergrade(number)
except:
    print("niepoprawna")