class Student:
    school_name="St Marys"
    def __init__(self,name,maths,eng,kisw,bio,phyc):
        self.name=name
        self.maths=maths
        self.eng=eng
        self.kisw=kisw
        self.bio=bio
        self.phyc=phyc

    def total_marks(self):
        self.total=self.maths+self.eng+self.kisw+self.bio+self.phyc
        return self.total

    def average(self):
        self.aver=self.total/5
        return self.aver

    def grade(self):
        average=self.aver

        if average >= 80 and average <= 100:
           return "A"
        elif average >= 75 and average <= 79:
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
        elif average >= 30 and average <= 34:
            return "D-"
        else:
            return "E"


bernard =student("Bernard",50,60,70,78,90)
print(bernard.total_marks())
print(bernard.average())
print(bernard.grade())








