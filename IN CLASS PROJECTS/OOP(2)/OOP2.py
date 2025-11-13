class Rectangle():
    def __init__(self, l,w):
        self.width = w
        self.length = l

    def rectangle_area(self):
        area = self.width*self.length
        return area

rectangle_object = Rectangle(23,67)
print("Area of the rectangle is",rectangle_object.rectangle_area()"CM2")