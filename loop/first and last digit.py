n=int(input())
t=0
def firstDigit(n) : 
    while n >= 10:  
        n = n / 10; 
    return int(n)
print (firstDigit(n))

def lastDigit(n) :
    return (n % 10)
print (lastDigit(n))
