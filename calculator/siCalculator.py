#Simple interest calculator
p=input("p:")
r=input("r:")
t=input("t:")
p=float(p)
r=float(r)
t=int(t)
SI=(p*r*t)/100
total=SI+p
print("Simple interest is :",SI)
print(total)