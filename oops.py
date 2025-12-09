# class Student:
#     def __init__(self):
#         self.__name = ""
#         self.__marks = 0

#     def set_details(self, name, marks):
#         self.__name = name
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks
#         else:
#             self.__marks = 0  # default if invalid

#     def get_details(self):
#         print("Name:", self.__name)
#         print("Marks:", self.__marks)
#         if self.__marks >= 50:
#             print("Grade: Pass")
#         else:
#             print("Grade: Fail")

# # main code
# n = int(input("How many students? "))

# for i in range(n):
#     name = input("Enter name: ")
#     marks = int(input("Enter marks: "))

#     s = Student()
#     s.set_details(name, marks)
#     s.get_details()



# import time

# start = time.time()
# input("Press Enter to stop: ")
# print("Elapsed Time:", round(time.time() - start, 2), "seconds")


# import calendar
# yr = int(input("enter year you want : "))
# mon = int(input("enter which month you want (1-12) :"))
# print(calendar.month(yr,mon))


# name = input("enter your name: ")
# age = int(input("enter your age (1-100): "))
# print(f"My name is {name} and I am {age} years old.")


# name = input("Enter your name: ")
# age = int(input("Enter your age (1–100): "))

# # Check age limit
# if 1 <= age <= 100:
#     print(f"My name is {name} and I am {age} years old.")
# else:
#     print("Age must be between 1 and 100!")
 
 
#  fibonacci series add a previous two numbers.
# n = 10
# a , b = 0 ,1
# print("Fibonacci series:")
# for i in range(n):
#     print(a,end=' ')
#     a , b = b , a+b


# factorial numbers 5!- 1*2*3*4*5
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(fact)


# using recurtion factorial
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))


# armstrong take number equal to exponential to the result is equal result
# num  = 153
# if 1**3 + 5**3 + 3**3 == num:
#     print("armstrong number")
# else:
#     print("not an armstrong number")


