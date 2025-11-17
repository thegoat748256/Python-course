class mysports():
    sport = "Football"

    def __init__(self,name,hobby):

        self.name = name
        self.hobby = hobby

    def promo(self):
        print("Hello, my name is",self.name)
        print("My favourite sport is",self.hobby)

Football = mysports("Joshua","football")
Football.promo()            