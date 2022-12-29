list_a=[1,2,3,5]
list_b=list_a
print(id(list_a));
print(id(list_b));
list_b[3]=4
print(list_a)
print(list_b)

list_a=[1000,2000]
list_b=list_a
list_a=list_a+[1000,2000]
print(str(list_a))
print(str(list_b))

a=[1,2,3,4,5,54,33,7,8]
b=a[10:1:-2]
print(b)

list_a=[10,20,30,40,70,56]
list_b=list_a[6:0:-1]
print(list_b)
list_b=list_a[::-1]
print(list_b)

m=500
n=4
m=str(m)
print(m*n)

m=500
n=4
m=str(m)
print(list(m*n))

'''a=[1,2,3,4,5,6,7,8,9]
print(a[0:3:]+a[6:9])
print(m[0:3]==n[0:3])

m=str(input())
n=str(input())
print(m[0:3]==n[0:3]


a=int(input())
b=int(input())
print(5*a//500 < 5*b%50)

m=70
p=60
c=60
print(m>=70 and p>=60 and c>=60)
print(m+p+c>=180)

s="rockybhai"
part=s[0:9:2]
print(part)

name="rockybhai"
print(name.lower())

name="rockybhai"
print(name.upper())

a="rockstar"
b=a.swapcase()
print(b)

a="rockstar"
b=a[::-1]
if(a==b):
    print("palindrome")
else:
    print("not palindrome")

for number in range(1,10):
    print(number)


n=list(map(int,input()))
sum=0
for i in n :
   sum=sum+i
print(sum)'''''
















