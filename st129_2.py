fhand = open ('mbox-short.txt')
for line in fhand :
    words = line.split()
    #print ('Debug :', words )
    if len(words) == 0 : continue
    if words [0] != 'From' : continue
    if len(words)==1 :continue
    print ( words [2])