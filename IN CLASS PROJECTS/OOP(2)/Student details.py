class Student_dtls():
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def disply(self):
        print("Name is",self.name)
        print("Mark is",self.mark) 

obj1 = Student_dtls("Joshua",100)
obj1.disply()
obj2 = Student_dtls("Jacob",99)
obj2.disply()           