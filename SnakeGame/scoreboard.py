from turtle import Turtle
ALIGNMENT = "center"
FONT= ("Arial",24,"noraml")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score :{self.score}", align ="center", font = ("Arial",24,"noraml"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Score :{self.score}", align ="center", font = ("Arial",24,"noraml"))



    def increase_score(self):
        self.score += 1
        self.write(f"Score :{self.score}", align =ALIGNMENT, font = FONT)
        self.clear()
        self.update_scoreboard()

