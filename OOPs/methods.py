class Student:
    school = "asmi"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3 

    def  avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.m3
    
    @staticmethod
    def info():
        print("this is inffo of school")

s1 = Student(98,97,99)
s2 = Student(89,90,95)
print(s1.avg())
print(Student.getschool())
Student.info()