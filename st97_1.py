text = 'X-DSPAM-Confidence: 0.8475'
numplace= text.find(" ")
liczba = text[numplace:]
liczba_f=float(liczba)
print(type(liczba_f))
print(liczba_f)
