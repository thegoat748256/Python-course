def no_notes(a):
    Q = [2000,500,200,100,50,20,10]
    x = 0
    for i in range (7):
        q = Q[i]
        x = a//q
        print("Number of",q,"is",x,".")
        a = a%q
amount = int(input("Please enter number of currency "))
no_notes(amount)