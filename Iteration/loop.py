# print a list of attendees
class_attendance=["Buom","Eunice","Keren","Richard","Kui","Sekina"]
print(class_attendance)

# adding an item in a list
class_attendance.append("Fridah")
print(class_attendance)

# print using indexing
'''print(class_attendance[0])
print(class_attendance[1])
print(class_attendance[2])
print(class_attendance[3])
print(class_attendance[4])
print(class_attendance[5])'''

# forloops
for each in class_attendance:
        print(each)

#  Tuple with a lislist
red=(["a","b","c","d","e","f","g","h"])
print(red[2])
# instead of indexing each use a for loop
for each in red:
    print(each)

# creating a list of elements btn 0-99
line=list(range(1,101))
print(type(line))
print(line)

# print even and odd
for each in line:
    if each%2==1:
        print("yaay")
    else:
        print("neey")
