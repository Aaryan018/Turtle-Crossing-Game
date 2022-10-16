from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-260, 260)
        self.write("Level: 1", align="left", font=FONT)


    def update_score(self, level):
        self.clear()
        self.write(f"Level: {level}", align="left", font=FONT)


    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", align="center", font=FONT)
