hour= float(input('Podaj ilość godzin')) 
rate= float(input('Podaj stawke godzinową')) 

def computepay(a,b):
    salery=(40*b)+((a-40)*b*1.5)
    return salery

x= computepay(hour,rate)
print('wynagrodzenie:' + str(x))