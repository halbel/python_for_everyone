def chop(t):
    del t[0]
    del t[-1]

climb= ["d",4,99,[2,3,4],"g"]
climb_b= chop(climb)
print(climb)
print(climb_b)
climd=[1,2,3,4,5,6,7]
def middle(t):
    return t[1:-1]
climd_c=middle(climd)
print(climd)
print(climd_c)