#Anonymous functions

#Add 5 to the number using lambda func
x=lambda a: a**2 
print("After adding 5 to given number(5)",x(5)) 

#Find greatest of two numbers using lambda
grt=lambda x,y: x if(x>y) else y
print("Greatest of 2,3",grt(2,3))

#Add 5 to the list of numbers using map func
lst=[2,4,3]
a=list(map(lambda x: x+5,lst))
print("After adding 5 to list of numbers",a)

#Perform square on list of numbers using map func
lst=[1,2,3]
sqr=list(map(lambda y: y*y,lst))
print("After performing square func",sqr)

#Print only even numbers from the given list using filter func
fib=[0,1,1,2,3,5,8,13,21,34]
f=list(filter(lambda x: x%2==0,fib))
print("Even numbers of the given list",f)

#Print only odd numbers from the given list using filter func
fib=[0,1,1,2,3,5,8,13,21,34]
f=list(filter(lambda x: x%2,fib))
print("Odd numbers of the given list",f)

#Print the sum of numbers present in the list using reduce func
from functools import reduce
lst=[1,2,3,4,5,6,7]
x=reduce(lambda x,y: x+y,lst)
print("Sum of the numbers in list",x)

