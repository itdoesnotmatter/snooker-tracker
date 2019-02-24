class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


    def __str__(self):
        return "({:>3},{:>3}):{})".format(self.x, self.y, self.color)
