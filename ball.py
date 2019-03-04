class Ball:
    def __init__(self, x, y, color):
        self.x = round(x, 3)
        self.y = round(y, 3)
        self.color = color


    def __str__(self):
        return "({:>3},{:>3}):{})".format(self.x, self.y, self.color)
