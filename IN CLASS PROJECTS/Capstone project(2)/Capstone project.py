# Importing the modules
import random
import pygame

class Button():
    def __init__(self,x,y,pos,width,height):
        self.x = x
        self.y = y
        self.pos = pos
        self.height = height
        self.width = width

    def Button_clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False
    

class Start_RPS():
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,1000))
        self.screen = pygame.display.set_caption("RPS brawl")

        self.bg = pygame.image.load("C:\Users\divya\OneDrive\Desktop\Python course\IN CLASS PROJECTS\Capstone project(2)\BG.png")
        
        self.Rock = pygame.image.load("C:\Users\divya\OneDrive\Desktop\Python course\IN CLASS PROJECTS\Capstone project(2)\ROCK.png").convert_alpha()
        self.Paper = pygame.image.load("C:\Users\divya\OneDrive\Desktop\Python course\IN CLASS PROJECTS\Capstone project(2)\PAPER.png").convert_alpha()
        self.Scissor = pygame.image.load("C:\Users\divya\OneDrive\Desktop\Python course\IN CLASS PROJECTS\Capstone project(2)\SCISSORS.png").convert_alpha()

        self.R_btn = pygame.image.load("C:\Users\divya\OneDrive\Desktop\Python course\IN CLASS PROJECTS\Capstone project(2)\Rock btn.jpg").convert_alpha()
        self.P_btn = pygame.image.load("C:\Users\divya\OneDrive\Desktop\Python course\IN CLASS PROJECTS\Capstone project(2)\paper btn.jpg").convert_alpha()
        self.S_btn = pygame.image.load("C:\Users\divya\OneDrive\Desktop\Python course\IN CLASS PROJECTS\Capstone project(2)\scissor btn.webp").convert_alpha()

        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.bg,(50,500))
        self.screen.blit(self.bg,(350,500))
        self.screen.blit(self.bg,(650,500))

        self.Rock_btn = Button(50,500, (50,500), (300,700))
        self.Paper_btn = Button(350,500, (350,500), (300,700))
        self.Scissor_btn = Button(650,500, (650,500), (300,700))

        self.font = self.font.Font(("Cursive"), 90)
        self.text = self.font.render(f'', True, (0, 0, 0))

        self.Player_Score = 0
        self.PC_Score = 0


    def Player_role(self):
        if self.Rock_btn.clicked(50):
            self.Player_option = "Rock"
            self.screen.blit(self.Rock, (120,200))

        elif self.Paper_btn.clicked(350):
            self.Player_option = "Paper"
            self.screen.blit(self.Paper, (120,200))

        elif self.Scissor_btn.clicked(650):
            self.Player_option = "Scissor"
            self.screen.blit(self.Scissor, (120,200))

        return self.Player_option


    def PC_role(self):
        self.PC_Random_Choice = " "
        Option = ["Rock", "Paper", "Scissor"]
        PC_Option = random.choice(list(Option))

        if PC_Option == "Rock":
            self.PC_Random_Choice = "Rock"
            PC_Option = self.Rock

        elif PC_Option == "Paper":
            self.PC_Random_Choice = "Paper"
            PC_Option = self.Paper

        elif PC_Option == "Scissor":
            self.PC_Random_Choice = "Scissor"
            PC_Option = self.Paper

        PC = self.screen.blit(PC_Option,(600,200))
        return PC
    
    