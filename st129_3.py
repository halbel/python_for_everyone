fhand = open ('mbox-short.txt')
for line in fhand :
    words = line.split()
    #print ('Debug :', words )
    if len(words) == 0 or words[0] !="From" or len(words)==1 : continue
  
    print ( words [2])