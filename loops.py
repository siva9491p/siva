n=list(map(int,input()))
sum=0
for i in n :
   sum=sum+i
print(sum)

n=int(input())
sum=0
for i in range(n):
    sum=sum+i
print(sum)

n=list(map(int,input()))
sum=1
for i in n:
    sum=sum*i
print(sum)

n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

n=int(input())
for i in range(n):
    for k in range((n-1)-i):
        print("*",end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range((n-(i+1):
        print(" ",end=" ")
        for k in range((i*2)-1):
            print("*",end=" ")
        print()


