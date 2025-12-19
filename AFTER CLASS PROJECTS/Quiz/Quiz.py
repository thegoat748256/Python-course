import sys

class Question():
    def __init__(self,Q,A,B,C):
        self.Q = Q
        self.A = A
        self.B = B
        self.C = C
Q1 = Question("1. Which is the team sport where only 5 men can play on a team?","A. Swimming","B. Basketball","C. Tennis")
Q2 = Question("2. Which team sport has a big bat and a striped ball?","A. Cricket","B. Volleyball","C. Baseball")
Q3 = Question("3. Which sport does not allow hands?","A. Basketball","B. Football","C. Volleyball")

def Start_Quiz():
    quiz = 1
    while quiz == 1:
        Wanna_play = input("Do you want to play the quiz? type yes or no. ")

        if Wanna_play == "yes" or Wanna_play == "YES":
            score = 0

            print("So you want to play, ok. You have 3 questions, answer them all, dont know, just guess. no negative marking. ")

            print(Q1.Q,"\n",Q1.A,Q1.B,Q1.C)
            Ans1 = input("Enter a choice (A/B/C): ")
            if Ans1 == "b":
             score = score + 1

            print(Q2.Q,"\n",Q2.A,Q2.B,Q2.C)
            Ans2 = input("Enter a choice (A/B/C): ")
            if Ans2 == "a":
                score = score + 1

            print(Q3.Q,"\n",Q3.A,Q3.B,Q3.C)
            Ans3 = input("Enter a choice (A/B/C): ")
            if Ans3 == "b":
                score = score + 1

            print("This is your score: ",score,"/ 3, Good job!")


        if Wanna_play == "no" or Wanna_play == "NO":
            quiz = 0
            sys.exit("Ok, thanks for playing! and have a nice day ahead! ")

    

print("Welcome to the quiz about sports! ")
Name = input("Before you start, Please enter your name. ")
print("Hello ",Name,"! ")
Start_Quiz()     