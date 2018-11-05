from config import nature
import time
import os


class mushroom1:
    def __init__(self, mario):
        self._type = 1
        self.direction = -1
        self.pos_x = mario.pos_x - mario.st - 1
        self.pos_y = mario.pos_y
        self.char = "|"

    def spawn(self, bd, mario):

        bd.array[self.pos_x][self.pos_y] = "|"
        bd.nature.append(self)

    def update(self, bd, mario):
        if(bd.nature[-1].char == "|"):

            bd.array[self.pos_x][self.pos_y] = " "
            if(bd.array[self.pos_x + 1][self.pos_y] == " "):
                self.pos_x += 1
            else:
                if(self.direction == 1):
                    self.pos_y += 1
                else:
                    self.pos_y -= 1
            if(bd.array[self.pos_x][self.pos_y] != " "):
                if(self.direction == 1):
                    self.pos_y -= 1
                    self.direction = -1
                else:
                    self.pos_y += 1
                    self.direction = 1
            bd.array[self.pos_x][self.pos_y] = "|"
            if(self.pos_x > 36):
                bd.nature.remove(self)
                bd.array[self.pos_x][self.pos_y] = " "
            if(self.pos_x == mario.pos_x and self.pos_y == mario.pos_y):
                bd.array[self.pos_x][self.pos_y] = " "
                if(mario.st == 1):
                    mario.st += 1
                elif(mario.st == 2 and bd.level == "2"):
                    mario.st += 1
                bd.nature.remove(self)


class bullets:
    def __init__(self, mario, bd):
        self._type = 1
        self.direction = 1
        self.active = 0
        self.char = "*"

    def spawn(self, mario, bd):
        if(self.active == 0):
            self.pos_x = mario.pos_x - mario.st
            self.pos_y = mario.pos_y + 1
            self.active = 1
            bd.power.append(self)
            bd.array[self.pos_x][self.pos_y] = "*"

    def update(self, bd, mario, boss):
        if(self.active == 1):
            if(bd.array[self.pos_x][self.pos_y + 1] == " "):
                bd.array[self.pos_x][self.pos_y] = " "
                self.pos_y += 1
                bd.array[self.pos_x][self.pos_y] = "*"
            elif(bd.array[self.pos_x][self.pos_y + 1] == "(" or bd.array[self.pos_x][self.pos_y + 1] == "#"):
                if(boss.lives == 1):
                    os.system("clear")
                    print("You Won!!")
                    exit()
                bd.array[self.pos_x][self.pos_y] = " "
                boss.lives -= 1
                self.active = 0
                bd.power.remove(self)
            else:
                bd.array[self.pos_x][self.pos_y] = " "
                bd.power.remove(self)
                self.active = 0
