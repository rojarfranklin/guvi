a=int(input())
total=0
i=1
while (i<=a):
    if (i%2)==0:
        print("{0}".format(i))
    i+=1
    total=total+i
print(total)
