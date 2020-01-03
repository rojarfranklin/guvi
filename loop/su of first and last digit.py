n=int(input())
swap=0
count=0
def firstDigit(n) : 
    while n >= 10:  
        n = n / 10; 
    return int(n)
print (firstDigit(n))
def lastDigit(n) :
    return (n % 10)
print (lastDigit(n))

while (n>0):
    n=n//10
    count+=1
print(count)

swap=((lastDigit(n))*(10**(count)))

swap=swap+((n%(10**(count))))

swap=swap-(lastDigit(n))

swap=swap+(firstDigit(n))

print(swap)

