import random
no_attemps = []
def score_displaying():
    if len(no_attemps) <= 0:
        print("There is currently no high score. Play this game to get a high score.")
    else:
        print("This is the highest score: ",min(no_attemps))

def Start_Game():
    RNG = int(random.randint(1,10))
    print("Hi! Welcome to the guessing game!")
    Player_Name = str(input("Before starting this game, Please enter your name. "))
    print("Hello ",Player_Name)
    Choice = input("Do you want to play the game? Type yes or no. ")
    Attemps_Made = 0
    score_displaying()
    while Choice.upper() == "YES":
        try:
            Guess = int(input("Please enter a number from 1 - 10. "))
            if Guess <1 or Guess >10:
                raise ValueError("The number is out of range, Please try again. ")
           
            if Guess <RNG:
                print("The number you entered is lower than the number generated.")
                Attemps_Made = Attemps_Made + 1

            if Guess >RNG:
                print("The number you entered is higher than the number generated. ")
                Attemps_Made = Attemps_Made + 1

            if Guess == RNG:
                print("Great job! you guessed my number! ")
                Attemps_Made = Attemps_Made + 1
                no_attemps.append(Attemps_Made)
                print("This is how many attempts you took to guess. Great job! :",Attemps_Made)
                Play_Again = input("Do you want to play again? Type yes or no. ")
                Attemps_Made = 0
                score_displaying()
                RNG = int(random.randint(1,10))
                if Play_Again.upper() == "NO":
                    print("Ok, visit again and have a great day ahead!")
                    break

        except ValueError as ERROR:
           print("This is not a valid input. Please try again. ")

if __name__ == '__main__':
    Start_Game()