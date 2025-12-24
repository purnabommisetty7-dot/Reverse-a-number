def factorial (n):
    out =1 
    while n>0:
       out=out*n
       n=n-1
    return out
n=int(input("Enter a number:"))
print(factorial(n))
    
    