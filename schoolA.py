from grade import find_total,average,find_grade

maths=int(input("enter maths score:"))
eng=int(input("enter eng score:"))
kisw=int(input("enter kisw score:"))
sci=int(input("enter sci score:"))
sst=int(input("enter sst score:"))

total_marks =find_total(maths,eng,kisw,sci,sst)
print(total_marks)

average=average(total_marks)
print(average)

average=find_grade(average)
print(average)