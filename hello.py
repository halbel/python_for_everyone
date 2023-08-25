try:
    hour= float(input('Podaj ilość godzin')) 
    rate= float(input('Podaj stawke godzinową')) 
    over = ((hour-40)*(rate*1.5))
    if hour > 40:
        print('Wynagrodzenie:' + str((40*rate)+ over))
    else:
        print(hour*rate)
except:
    print("podaj wartośc numeryczną")