## Fibonacci series upto 3 digits
#a,b = 0,1
#while b < 1000:
#    print (b, end=' ', flush=True)
#    a, b = b, a+b

## Fibonacci for nth fibonacci number
#def fibonacci (n):
#    a,b = 0,1
#    for counter in range(3, n+1):
#        a,b = b,a+b
#        if counter == n:
#            return b         
#print (fibonacci (int(input("Enter position number for fibonacci series:"))))


## Fibonacci using Recursive function call

#def fibonacci (n):
#    if n<=0:
#        print ("Incorrect input")
#    elif n==1:
#        return 0
#    elif n==2:
#        return 1
#    else:
#        return fibonacci(n-1) + fibonacci(n-2)
    
#print (fibonacci(4))


## A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
import math
def isperfectsquare(n):
    s = (5*n**2 + 4)
    r = (5*n**2 - 4)
    s2 = int(math.sqrt(s))
    r2 = int(math.sqrt(r))
    return (s2**2 == s) or (r2**2 == r)
num = int(input("Enter the number to be evaluated "))
if isperfectsquare(num) == True:
    print('Number {} is a Fibonacci number'.format(num))
else:
    print('Number {} is not a fibonacci number'.format(num))
