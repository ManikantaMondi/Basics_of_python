# a=int(input("Enter any number :"))
# if a%3==0 and a%6==0:
#     print("Good number")
# elif a%2==0 and a%7==0:
#     print("Average number")
# elif a%9==0 or a%4==0:
#     print("Awesome Number")
# else:
#     print("Bad Number")


# p=int(input("Enter Bike Price :"))
# if p>72000 and p<150000:
#     tax=p*(10/100)
#     insurance=p*(15/100)
#     price=p+tax+insurance
#     print(price)
# elif p>=150000 and p<200000:
#     tax=p*(25/100)
#     insurance=p*(20/100)
#     price=p+tax+insurance
#     print(price)
# elif p>=200000:
#     tax=p*(35/100)
#     insurance=p*(28/100)
#     price=p+tax+insurance
#     print(price)
# else:
#     print("Bike Price Start From 72000")

# y=int(input("Enter the year number"))
# if (y%4==0 and y%100!=0) or y%400==0:
#     print("leap year :",y)
# else:
#     print("Not a Leap year")

# a=int(input("Enter the first side value:"))
# b=int(input("Enter the second side value:"))
# c=int(input("Enter the third side value:"))
# if(a==b==c):
#     print("Equilateral Triangle")
# elif(a==b or b==c or c==a):
#     print("isosilus")
# else:
#     print("scalar")

# fact=1
# for i in range(1,8):
#     fact=fact*i
# print(fact)


# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")
# for i in range(3,11):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c

# n=int(input("Enter number :"))
# flag=0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break
# if flag==1:
#     print("not")
# else:
#     print("prime")

# for i in range(1,6):
#     for s in range(1,5-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,6):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6-i+1):
#         print("*",end="")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         if(i==1 or i==4 or j==1 or j==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="") 
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# n=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(n,end=" ")
#         n=n+1
#     print()

# for i in range(1,5):
#     for j in range(1,8):
#         if i==4:
#             print(j)
        
# for i in range(1,5):
#     for d in range(4-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print( )

# n=int(input("enter any number :"))
# while n>0:
#     r=n%10
#     print(r)
#     n=n//10

# n=int(input("enter any number"))
# p=0
# while n>0:
#     r=n%10
#     p=p+r
#     n=n//10
# print(p)




# n=int(input("enter any number :"))
# n1=n
# sum=0
# while n>0:
#     r=n%10
#     sum=sum+r
#     n=n//10
# if n1/sum==0:
#     print("it is divisible by sum")
# else:
#     print("not divisible")

# n=int(input("enter any number :"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum>n:
#     print("yes")
# else:
#     print("no")

# n=int(input("enter any number"))
# sum1=0
# sum2=0
# for i in range(1,n+1):
#     if i%6==0:
#         sum1=sum1+i
#     else:
#         sum2=sum2+i
# diff=sum2-sum1
# print(sum1)
# print(sum2)
# print(diff)

# n=int(input("enter any number :"))
# t=n
# num=0
# while n>0:
#     r=n%10
#     num=num*10+r
#     n=n//10
# print(num)
# if t==num:
#     print("yes")
# else:
#     print("no")

# n=int(input("enter any number"))
# nod=0
# n1=n
# org=n
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print(count)

# FUNCTIONS TOPICS

# def fun(a,b):
#     b=int(b)
#     c=a*b
#     print(c%10)
# a=int(input("Enter a value :"))
# b=int(input("Enter b value :"))
# fun(a,b)

# def func(a,b):
#     c=a+b
#     print(c)
# a=int(input("enter a"))
# b=int(input("enter b"))
# func(a,b)

# unknown arguments
# def func(**name):
#     print("my name is",name["fname"])
#     print("my name is",name["lname"])
# func(fname="prashant", lname="sharma")

# def fun(a):
#     c=a%10
#     while(a>=10):
#         a=a//10
#     print(a+c)
# a=int(input("enter a value :"))
# fun(a)

# def fun():
#     a=input("Enter User Name:")
#     b=input("enter password:")
#     if(a==b):
#         print("Log in success ")
#         return True
#     return False
# while True:
#     if (fun()):
#         break

# def fun():
#     a=input("Enter User Name:")
#     b=input("enter password:")
#     if(a==b):
#         print("Log in success ")
#         return True
#     else:
#         print("You have entered wrong data")
# while True:
#     if (fun()):
#         break

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# c=int(input("Enter the number:"))
# res=fact(c)
# print(res)

# def fab(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# c=int(input("Enter the number :"))
# r=fab(c)
# print(r)

# def rev(n):
#     if n==0:
#         return
#     print(n%10)
#     return rev(n//10)
# rev(12345)

# def digit(n):
#     if(n==0):
#         return 0
#     return 1+digit(n//10)
# print(digit(12345))

# def sum(n):
#     if(n==0):
#         return 0
#     return n%10+sum(n//10)
# print(sum(12))

# def count(n):
#     if n==0:
#         return 0
#     else:
#         return 1+count(n//10)
# def arm(n):
#     global r
#     if n==0:
#         return 0
#     else:
#         re=n%10
#         return re**r+arm(n//10)
# num=int(input("Enter the number :"))
# r=count(num)
# a=arm(num)
# if num==a:
#     print("Yes")
# else:
#     print("No")/

# #creating list
# list=[1,3,23,4,5,34,23]
# print(list)
# #accesing list
# print(list[3],list[2],list[5],list[-1])

# #slicing list

# print(list[:4])
# print(list[::2])

# #loops accessing
# for i in list:
#     print(i,end=" ")
# print()

# #append
# lis1=list.append(65)
# for i in list:
#     print(i)

# #insert

# list.insert(5,99)
# print(list)


# lis=[12,42,23,96,7,18,10,133]
# mini=0
# maxi=0

# for i in range(len(lis)):
#     if mini>list[i]:
#         mini=list[i]
#         miniid=i
#     if maxi<lis[i]:
#         maxi=lis[i]
#         maxiid=i
# s=mini+maxi
# d=maxi-mini
# lis[miniid]=d
# lis[maxiid]=s


# dic={"id":"1","name":"mani","education":"b.tech","city":"rajahmundry"}
# print(dic["name"]," ",dic["city"])

# list=[22,42,65,1,-4,6,-1]
# m1=999
# m2=999
# for i in list:
#     if i<m1:
#         m2=m1
#         m1=i
#     elif m2>i and m2>m1:
#         m2=i
# print(m2)

# set={1,2,3,4,5,6}
# print(set)

# set.add(7)
# print(set)

# fs=frozenset(set)
# print(set)


a=[2,0,1024,0,40,230,0]
for i in a:
    if i>0:
        print(i,end=" ")
for i in a:
    if i==0:
        print(i,end=" ")