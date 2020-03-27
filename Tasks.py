# TASK 1
'''program to output gender'''
'''gender=(input("What is your gender:"))
if gender=="female":
     print("yes")
elif gender=="male":
    print("no")
else:
     print("invalid")'''

# TASK 2
'''function that compares numbers'''
def compare():

     num1=int(input("enter num1:"))
     num2=int(input("enter num2:"))
     num3=int(input("enter num3:"))

if num1>num2 and num1>num3:
        print("num1 is greater")
elif num2>num1 and num2>num3:
        print("num2 is greater")
elif num3>num1 and num3>num2:
        print("num3 is greater")

compare()

# TASK 3
'''function with a list'''
'''def my_list():
    list=[1,2,3,4,5]
    list2(list[0],list[4])
    print(list 2)
my_list()'''

# TASK 4
'''print even or odd'''
'''def even_odd(x):
     if x%2==0:
          return "even"
     else:
          return "odd"
num=int(input("Enter your number:"))
print(even_odd(num))'''

# TASK 5
'''print half and last part of a tuple'''
def split_the_tuple(atuple):
     # find the midpoint
     half = int(len(atuple/2))

     # get the first and the last haf of the tuple
     first_half = atuple[:half]
     last_half = atuple[half:]

     # convert halfs to strings
     first_half_toString = str(first_half)
     first_half_toString = str(last_half)

     # use the string function in python that returns a copy of the string with both leading
     first_half_values = first_half_toString.strip('()')
     last_half_values = last_half_toString.strip('()')

     print(split_the_tuple(first_half_values))
     print(split_the_tuple(last_half_values))

# split_the_values ((1,2,3,4,5,6,7,8,9,10))