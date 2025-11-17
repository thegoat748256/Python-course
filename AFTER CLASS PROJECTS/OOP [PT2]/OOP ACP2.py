class Circle():
   
    def __init__(self,R):
        self.radius = R
        
    def circle_area(self):
        return self.radius*self.radius*3.14

    def circle_circum(self):
        return 2*3.14*self.radius

newCircle = Circle(0)
print("Radius of the circle is",newCircle.radius)
print("Area of the circle is",newCircle.circle_area())
print("Circumference of the circle is",newCircle.circle_circum())