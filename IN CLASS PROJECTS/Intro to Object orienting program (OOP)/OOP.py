class  birds:
    Species =  "Bird"

    def __init__(self,age,color):

        self.age = age
        self.color = color

blu = birds(5,"blu")
woo = birds(3,"woo")

print("blu is a",blu.Species)
print("woo is a",woo.Species)

print("Blu`s age is",blu.age)
print("Blu`s` color is",blu.color)

print("woo`s age is",woo.age)
print("woo`s` color is",woo.color)