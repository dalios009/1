from math import*

a=int(input("donner a"))
b=int(input("b"))
c=int(input("c"))
d=b*b-4*a*c


print("delta= ",d)
if d>0  :
    print("delta>0")
    print("donc f a deux racines")
    print("x1=",'{0:.2}'.format((-b-sqrt(d))/(2*a)))
    print("et x2=",'{0:.2}'.format((-b+sqrt(d))/(2*a)))
elif d==0:
    print("delta est null")
    print("donc f a une racine")
    print("x1=",-b/2*a)
else:
    print("delta estt negative donc f n a pas de racine " )
