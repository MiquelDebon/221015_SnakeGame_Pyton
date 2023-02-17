from turtle import Turtle
FONT = "Arial", 15, "normal"
FONT_OVER = "Arial", 25, "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 250)
        self.write(f"Score: {self.score}", True, align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.setposition(0, 250)
        self.score += 1
        self.write(f"Score: {self.score}", True, align="center", font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("Game Over", True, align="center", font=FONT_OVER)