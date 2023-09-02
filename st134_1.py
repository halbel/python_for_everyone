fhand=open('words.txt', encoding="UTF-8")
words=dict()
import string
for line in fhand:
    line=line.translate(str.maketrans(' ',' ', string.punctuation))
    line=line.lower()
    xxx=line.split()
    for x in xxx:
        if x not in words:
            words[x]=0
   
    

print(words)