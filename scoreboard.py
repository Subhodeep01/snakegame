from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.file = ''
        self.high_score = 0
        self.scr = 0
        self.readfile()
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.scr}, High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def score(self):
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.scr}, High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def highscore(self):
        if self.high_score < self.scr:
            self.high_score = self.scr
        self.writefile()
        self.scr = 0
        self.score()

    def update(self):
        self.scr += 1
        self.score()

    def readfile(self):
        self.file = open("High_Score.txt", mode="r")
        self.high_score = int(self.file.read())
        self.file.close()

    def writefile(self):
        self.file = open("High_Score.txt", mode="w")
        self.file.write(str(self.high_score))
        self.file.close()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
