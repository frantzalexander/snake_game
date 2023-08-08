from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Scoreboard: {self.score} High Score {self.highscore}", 
            move = False,
            align = ALIGNMENT, 
            font = FONT
            )
    
    def reset(self):
        
        if self.score > self.highscore:
            self.highscore = self.score
            with open ("highscore_data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
            
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()