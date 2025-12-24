def reverse(n):
    out=0
    store=n
    while n>0:
         rem=n%10
         out=out*10+rem
         n=n//10
    if store==out:
       return ("palindrometric number")
    else:
       return("not a palindrometric number")
      
n=int(input("Enter the number:"))      
print(reverse(n))
  