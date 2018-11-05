import powers
import time
from config import nature


class Obstacle:
    def __init__(self):
        self.char = "X"

    def process(self, bd, mario, next_piece, bullet):
        p1 = point_block()
        p2 = powerup_block()
        p3 = brick()
        p4 = spring()
        if(next_piece == p1.char):
            next_piece = point_block()
            if(next_piece.on_hit(bd, mario, bullet) == 1):
                return "break"
            else:
                return ""
        elif(next_piece == p2.char):
            next_piece = powerup_block()
            if(next_piece.on_hit(bd, mario, bullet) == 1):
                return "break"
            else:
                return ""
        elif(next_piece == p3.char):
            next_piece = brick()
            if(next_piece.on_hit(bd, mario, bullet) == 1):
                return "break"
            else:
                return ""
        elif(next_piece == "G"):
            return "kill"
        elif(next_piece == p4.char):
            next_piece = spring()
            if(next_piece.on_hit(bd, mario, bullet) == 1):
                return "jump"
            return "jump"
        return "kill"


class brick(Obstacle):
    def __init__(self):
        self.char = 'O'

    def __repr__(self):
        return "O"

    def on_hit(self, bd, mario, bullet):
        if(mario.st == 1):
            return 0
        if(mario.st == 2):
            return 1


class point_block(Obstacle):
    def __init__(self):
        self.char = 'P'
        self.state = 0

    def __repr__(self):
        if(self.state == 0):
            return "P"
        else:
            return "B"

    def on_hit(self, bd, mario, bullet):
        if(self.state == 1):
            return -1
        self.state = 1
        bd.array[mario.pos_x - mario.st][mario.pos_y] = "B"
        mario.score += 1
        return 0


class powerup_block(Obstacle):
    def __init__(self):
        self.char = 'M'
        self.state = 0

    def __repr__(self):
        if(self.state == 0):
            return "M"
        else:
            return "B"

    def on_hit(self, bd, mario, bullet):
        if(self.state == 1):
            return -1
        self.state = 1
        power = powers.mushroom1(mario)
        power.spawn(bd, mario)
        bd.array[mario.pos_x - mario.st][mario.pos_y] = "B"
        return 0


class Ghost():
    def __init__(self, bd, pos_x, pos_y, priority):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.char = "G"
        self.direction = -1
        self.leg = self.pos_x
        self.head = self.pos_x + 1
        bd.nature.append(self)
        self.active = 0
        self.timr = time.clock()
        self.priority = priority

    def spawn(self, bd, mario):
        bd.array[self.pos_x][self.pos_y] = "G"
        bd.nature.append(self)

    def on_hit(self, bd, mario, bullet):
        bd.array[self.pos_x][self.pos_y] = " "
        bd.array[self.pos_x - 1][self.pos_y] = " "
        bd.nature.remove(self)
        mario.score += 10
        return 0

    def update(self, bd, mario):
        if(self.active % self.priority == 0):
            bd.array[self.pos_x][self.pos_y] = " "
            bd.array[self.pos_x - 1][self.pos_y] = " "
            if(bd.array[self.pos_x + 1][self.pos_y] == " "):
                self.pos_x += 1
            else:
                if(self.direction == 1):
                    self.pos_y += 1
                else:
                    self.pos_y -= 1
            if(bd.array[self.pos_x][self.pos_y] != " " or bd.array[self.pos_x - 1][self.pos_y] != " "):
                if(self.direction == 1):
                    self.pos_y -= 1
                    self.direction = -1
                else:
                    self.pos_y += 1
                    self.direction = 1
            bd.array[self.pos_x][self.pos_y] = "G"
            bd.array[self.pos_x - 1][self.pos_y] = "G"
        #    print(self.char," ",self.pos_x," ",self.pos_y," hi")
            if(self.pos_x == mario.pos_x and self.pos_y == mario.pos_y):
                print(self.char, " ", self.pos_x, " ", self.pos_y)
                if(mario.st == 1):
                    bd.array[self.pos_x][self.pos_y] = " "
                    mario.restart(bd)
                else:
                    mario.st -= 1
            self.active = 1
        else:
            self.active += 1


class spring(Obstacle):
    def __init__(self):
        self.char = "!"

    def on_hit(self, bd, mario, bullet):
        timer = 12
        mario.medium = 1
        bd.jump_mario(mario, self.char, timer, bullet)
        return 1
