from config import nature
import config
import time
import os
from copy import deepcopy
from random import randint
from objects import Ghost


class Mario():
    def __init__(self):
        self.pos_x = 30
        self.pos_y = 20
        self.leg = self.pos_x
        self.head = self.pos_x - 1
        self.medium = 0
        self.score = 0
        self.level = 0
        self.st = 1
        self.vy = 0
        self.lives = 3
        self.start = time.clock()
        self.prev = self.start

    def is_ok(self, board):
        for i in range(self.st + 1):
            if(board.array[self.pos_x - i][self.pos_y] != ' '):
                return False
        return True

    def restart(self, bd):
        '''initialize all objects again'''
        os.system("clear")
        print("Remaining Lives = ", self.lives - 1)
        print(" #", "\n", "I x ", self.lives - 1)
        time.sleep(2)

        bd.init_board()
#        ghost1 = Ghost(35,69)
        if(self.lives == 1):
            print("Game Over!", "Your Score is",
                  self.score * (bd.totaltime - bd.timer))
            exit()
        bd.timer = bd.totaltime
        self.start = time.clock()
        self.lives -= 1
        self.score = 0
        bd.frame = 0
        self.pos_x = 30
        self.pos_y = 20
        self.st = 1

    def level_done(self, bd):
        while(bd.array[self.pos_x][self.pos_y - 1] != "(" or bd.array[self.pos_x][self.pos_y + 1] != ")"):
            self.pos_y += 1
            bd.print_board(self.pos_x, self.pos_y, self)
        os.system("clear")
        print("Game over!!", "  Score = ", self.score)
        exit()


class Boss_enemy():
    def __init__(self, bd):
        self.char = "#"
        self.pos_x = 30
        self.width = 1
        self.lives = 3
        self.height = 3
        self.pos_y = 150
        self.timr = time.clock()
        self.kimr = time.clock()
        self.simr = time.clock()
        self.lives = 3
        self.shout = 0
        bd.nature.append(self)

    def update(self, bd, mario):
        var = randint(0, 1)
        if(time.clock() - self.timr > 0.1):
            self.timr = time.clock()
            self.shout = 0
            bd.array[self.pos_x -
                     self.height][self.pos_y -
                                  self.width -
                                  1] = " "
            bd.array[self.pos_x -
                     self.height][self.pos_y -
                                  self.width -
                                  2] = " "
            bd.array[self.pos_x -
                     self.height][self.pos_y -
                                  self.width -
                                  3] = " "

        if(var == 1 and time.clock() - self.kimr > 0.5 and bd.nature[-1].char != "|"):
            self.shout = 1
            bd.array[self.pos_x -
                     self.height][self.pos_y -
                                  self.width -
                                  1] = "("
            bd.array[self.pos_x -
                     self.height][self.pos_y -
                                  self.width -
                                  2] = "("
            bd.array[self.pos_x -
                     self.height][self.pos_y -
                                  self.width -
                                  3] = "("
            ghostly = Ghost(bd, 30, randint(153, 158), 1)
            self.kimr = time.clock()
        if(time.clock() - self.simr > 0.7):
            if(bd.nature[-1].char == "G"):
                self.simr = time.clock()
                obj = bd.nature[-1]
                bd.array[obj.pos_x][obj.pos_y] = " "
                bd.array[obj.pos_x - 1][obj.pos_y] = " "
                bd.nature.remove(bd.nature[-1])
