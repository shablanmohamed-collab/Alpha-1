# a = 10
# b = 20
# c = 30

# print(a,b,c)
# print("A = ",a,"B = ",b,"C = ",c)
# print("A = {} B = {} C = {}".format(a,b,c))
# print (f"A = {a} B = {b} C = {c}")

# print(10+5)
# a=90
# print(a)
# print(10-5)
# print(10*5)
# print(10/5)
# print(50%5) 
# print(15//5)
# print(2**4)

# a = 5

# a += 5     #--->  a = a + 5
# a -= 5     #--->  a = a - 5
# a *= 5     #--->  a = a * 5
# a /= 5     #--->  a = a / 5
# a %= 5     #--->  a = a % 5
# a //= 5    #--->  a = a // 5
# a **= 5    #--->  a = a ** 5
# print(a)

b = 10

# b += 5     #--->  b = b + 5
# b -= 5     #--->  b = b - 5
# b *= 5     #--->  b = b * 5
# b /= 5     #--->  b = b / 5
# b %= 5     #--->  b = b % 5
# b //= 5    #--->  b = b // 5
# b **= 5    #--->  b = b ** 5

# print(b)

# age = 20

# print(age > 21)
# print(age < 21)
# print(age == 21)
# print(age != 21)
# print(age >= 21)

# print(age <= 21)

# age = 20

# student = True

# print(age > 30 and student)

# 0    0 - False
# 0    1 - False
# 1    0 - False
# 1    1 - True 

# age = 20 

# student = True

# print(age > 30 or student)

# 0  0 - False
# 0  1 - True
# 1  0 - True
# 1  1 - True

# student = True 

# print(not student)

# my_list = [1,2,3,4]

# print(1 not in my_list)

# a={1,2,3}

# b = a 

# c = {1,2,3}

# a,b,c = 1,2,"hello"

# print(a)
# print(b)
# print(c)

# a,b = 10,20

# a,b = b,a

# print(a)
# print(b)

# c=a
# a=b
# b=c

# person = ("john", "doe", 30)

# firstname, lastname, age = person

# print(firstname)
# print(lastname)
# print(age)

# int

# float
# b = 10.5

# string
# c = "hello world"
# print(len(c))
# print(c[0:10:2])
# print(c[:])
# print(c[0])
# print(c[-1])
# print(c[0:5])
# print(c[5:])

# boolean
# d = True

# list
# e = "hello world"
# print(len(c))
# print(c[0:10:2])
# print(c[:])
# print(c[0])
# print(c[-1])
# print(c[0:5])
# print(c[5:])

# tuple 
# f = "hello world"
# print(len(c))
# print(c[0:10:2])
# print(c[:])
# print(c[0])
# print(c[-1])
# print(c[0:5])
# print(c[5:])

# set
# g = {1,2,3,"apple"}

# f = set((1,2,3,"apple"))
# for i in f:
#     print(i)

# dictionary
# h = {"name" : "john","age" : 30}
# print(h["name"])

# x=5
# if x>0:
#     print("x is positive")

# age= int(input("Enter age:"))
# if age >= 18:
#     print("Eligible")
# else:
#     print("not Eligible")

# x = int(input('enter a number:'))
# if x<0:
#     print('postive')
# elif x<0:
#     print('negative')
# else:
#     print('number is zero')

# age = 20
# citizen = True
# if age >= 18:
#     if citizen:
#         print("you are eligible to vote.")
# else:
#     print("you must be a citizen to vote.")
# else:
#     print("you are not old enough to vote.")18

# name = ("python")
# for i in name:
#      print(i)

# name = ("python")
# for i in name:
#      print(i,end="")

# person = {"name":"john","age":30,"city":"NEW YORK"}
# for i in person:
#     print(person[i])

# for key,value in person.items():
#     print(key,":",value)

# for i in range (5):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(1,6):
#     print(f"count : {i}")

# for i in range(10,0,-1):
#     print(i)

# matrix = [{1,2,3},{4,5,6},{7,8,9}]
# for i in matrix:
#     for j in i:
#         print(j,end=" ")
#         print()

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# for i in range(0,10):
#     if i==5:
#         break
#     print(i)

# for i in range(0,10):
#     if i==5:
#         continue
#     print(i)

# i=0
# for i in range(0,5):
#     pass
# print(i)


"""/////////////////////////"""

# count = 0
# # Windsurf: Refactor | Explain | Generate Docstring | X
# def increment(): 
#     global count
#     count += 1


# increment()
# increment()
# print(count)

# def recursive_function(parameters):
#     if base_case_conditions:
#         return value
#     else:
#         return recursive_function(modified_parameters)
    
# def factorial(n):
#     if n == 0: 
#         return 1
#     else:
#         return n * factorial(n - 1) 
# print(factorial(5))

# def sum_upto(n):
#     if n == 1: 
#         return 1
#     else:
#         return n * factorial(n - 1) 
# print(factorial(5))

# def sum_list(lst):
#     if len(lst) == 0:
#        return 0
#     else:
#         return lst[0] + sum_list(lst[1:])
    
#     print(sum_list([1, 2, 3, 4]))
    
    
# def revers_string(s):
#     if len(5) == 0:
#        return s
#     else:
#         return revers_string(s[1:]) + s[0]
# print(revers_string("hello"))


# lambda arguments: expression 
    
# square = lambda x: x * x
# print(square(5))

# add = lambda a, b: a + b
# print(add(3, 5))

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
