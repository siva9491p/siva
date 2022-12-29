n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

n=int(input())
for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end=" ")
    for k in range((i*2)+1):
        print("*",end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end=" ")
    for k in range((i*2)+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range