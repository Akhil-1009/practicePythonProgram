class student():
    institution="iips"
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def show(self):
        print("marks in python =",self.a)
        print("marks in python lab =",self.b)
    @classmethod
    def info(self):
        print("class belongs to ",self.institution)
    @staticmethod
    def about():
        print("this class is about the marks obtained")

s1=student(12,10)
s2=student(13,11)
s3=student(14,9)
s1.show()
s2.show()
s3.show()
student.info()
student.about()