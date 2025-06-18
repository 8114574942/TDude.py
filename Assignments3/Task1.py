



def factorial(n):
    if n<2:
        return 2
    else:
     return n*(factorial(n-1))

result=factorial(5)    
print(result)