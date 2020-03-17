def even_odd(p,d):

    if p%2==0:
        print("even")
    else:
        print("odd")
    print(d)

even_odd(4,"thanks")
# calling a function wou

# def is used for function declaration
# even_odd is the name of the function we want to carry out
# p is a variable
# method is a function declared
# the variable p is a parameter ;they may be more than one
# a parameter is a variable that tells a fuction how many values to expect as input
# arguments are inputs to our functions
# my arguments are 4 and thanks ...assigned to p and d
# how we would use functions to add

# def sum(a,b,c):
#      print(a+b+c)
#  sum(2,3,4)

'''def test(name="jane"):
     print("president {}".format(name))
test()
# name="kingston"

# concutination is adding strings together
print("mango"+" "+"eggs")'''

# string formatting
# 1.fstring
'''name=input("What is your name:")
name="kivuti"
print(f"My name is:{name}")'''

# example 2:
'''fruit=input("What is favourite fruit:")
fruit="apple"
print(f"My favourite fruit is:{fruit}")'''

# 2.string formatting


# args unlimited positional arguments
def sumn(*args):
    print(args)

total=0
for each in args:
#lists them
    total+=each
sumn(10,40,80,10)
