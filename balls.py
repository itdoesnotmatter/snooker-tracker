from ball import Ball


class Balls:
    def __init__(self):
        self.__balls = []


    def to_list(self):
        return self.__balls


    def add(self, x, y, color):
        self.__balls.append( Ball(x, y, color) )


    def __str__(self):
        balls = ", ".join( map(str, self.__balls) )
        return "[{}]".format( balls )
