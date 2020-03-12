
# displaylength
names = "wanjiku"

print(len(names))

# lists
names = ["Dan", 1, "tim", True, False, 10.2]

print(names)

# indexing a character in a list
print(names[3])
print(names[5])

matrix = [[1, 2, 3],[4, 5, 6,["a", "b", "c", "d", [11, 12, 13]]],[7, 8, 9]]

# accessing element 6 which is in a list inside a list
print(matrix[1][2])

# list nesting to get d
print(matrix[1][3][-1])

# nesting to get 12
print(matrix[1][3][4][1])

# popping is removing an element from a list
numbers=[1, 2, 3, 4, 5, 6, 7,8 ]
numbers[2]=11
numbers.pop()
print(numbers)

# appending is more of adding
empty=[2]
print(empty)
empty.append(1)
print(empty)

# print(name.replace())
# tuple is immutable;it cant be changed
days=("mon","tue","wed","thur","fri","sat","sun")
print(days)
print(days[3])

# selecting in a tuple
username="Mark zuckerberg"
password="pwd"

# print username
mydbvalues=(1,"Mark zuckerberg","password",30,"male")
un=mydbvalues[1]
print(un)

# print password
pss=mydbvalues[2]
print(pss)

# ==strict equality operator
# checking if the username is right
# assignment operator
if un==username:
    print("username true")
else:
    print("username false")

# checking password
if pss==password:
    print("password true")
else:
    print("wrong password")

# Dictionaries
dict=10
print(dict)

myDictionary={"username":"markzukerberg","password":"pwd","age":30,"sex":"male"}
print(myDictionary["username"])
print(myDictionary["password"])
print(myDictionary["age"])

# # self={
#     "firstname":"yuna",
#     "lastname":"wanjiku"
#     "schools": "primary schools"[
#     "school name" = "kianjeru"
# ]

dict{
    "user":"yuna"
    "age":11
}
print(dict["age"])