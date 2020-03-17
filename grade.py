def find_total(maths,english,kiswahili,science,sst):
     total=maths+english+kiswahili+science+sst
     return total
x=find_total(maths=50,english=50,kiswahili=50,science=50,sst=50)
print(x)
# find average
def average(total):
 average=(total/5)
 return average
y=average(x)
print(y)

# grading
def find_grade(average):

    if average >= 80 and average <= 100:
        return "A"
    elif average >=75 and average <= 79:
       return "A-"
    elif average >= 70 and average <= 74:
        return "B+"
    elif average >= 65 and average <= 69:
        return "B"
    elif average >= 60 and average <= 64:
        return "B-"
    elif average >= 55 and average <= 59:
        return "C+"
    elif average >= 50 and average <= 54:
        return "C"
    elif average >= 45 and average <= 49:
        return "C-"
    elif average >= 40 and average <= 44:
        return "D+"
    elif average >= 35 and average <= 39:
        return "D"
    elif average>=30 and average <= 34:
        return "D-"
    else:
          return "E"

print(find_grade(y))