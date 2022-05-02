class circle:
    def __init__(self,radius1):
        self.radius=radius1
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius
a=int(input("enter the value of radius"))
c1=circle(a)
result=c1.area()
result1=c1.circumference()
print("area is ",result,"circumference is ",result1)