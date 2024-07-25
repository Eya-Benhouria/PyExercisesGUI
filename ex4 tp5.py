

from random import *
def rang():
    u0=randint(3,40)
    print(u0)
    pos=1
    while u0!=4:
        if u0%2==0:
            un=u0/2

        else:
            un=3*u0+1
            u0=un
            pos+=1
        return pos
print("le rang=",rang())
