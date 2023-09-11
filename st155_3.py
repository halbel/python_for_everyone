fhand=open((input("enter the file name:")), encoding="utf8" )
letters=dict()
import string

print(fhand)
for line in fhand:
    line=line.translate(str.maketrans(" "," ",string.punctuation))
    line=line.lower()
    word=line.split()
    for letter in word:
        if letter not in letters:
            letters[letter]=1
        else:
            letters[letter]+=1

new_area="".join(letters)
finish=dict()
for l in new_area:
    if l not in finish:
        finish[l]=1
    else:
        finish[l]+=1

finish2=list(finish.items())
finish2.sort()
print(finish2)
