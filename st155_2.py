fhand=open(input("enter the file name:"))
data=dict()
for line in fhand:
    if not line.startswith("From "):continue
    words=line.split()
    word=words[5]
    hours=word.split(":")
    hour=hours[0]
    if hour not in data:
        data[hour]=1
    else:
        data[hour]+=1
print(data)
datas=list(data.items())
datas.sort()

for key,val in datas:
    print(key, val)