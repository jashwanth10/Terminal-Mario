import os
import sys
from sys import stdout
from players import Boss_enemy
import time
import random
import config
from objects import Obstacle
import powers
from copy import deepcopy
from objects import Ghost
import maps
from colorama import *


class Board:
    def __init__(self, level):
        self.width = 500
        self.height = 40
        self.frame = 0
        self.array = []
        self.buff = []
        self.arr = []
        self.buf = []
        self.flag = 17
        self.ld_y, self.rd_y = 35, 35
        self.lu_x, self.ru_x = 1, 98
        self.lu_y, self.ru_y = 1, 1
        self.ld_x, self.rd_x = 1, 98
        self.totaltime = 180
        self.timer = self.totaltime
        self.level = level

    def init_board(self):
        self.nature = []
        self.power = []
        if(self.level == "1"):
            map = maps.map1()
        else:
            map = maps.map2()
            boss = Boss_enemy(self)
        map.init_map(self)
        self.array = map.array
        # config.level.append(self.array)

    def print_board(self, x, y, mario):
        sys.stdin.flush()
        t = self.frame
        if(time.clock() - mario.prev >= 0.25):
            mario.prev = time.clock()
            self.timer -= 1
            if(self.timer <= 0):
                mario.restart(self)
        if(mario.pos_x - mario.st >= 30):
            mario.restart(self)
        self.update_nature(mario)

        if(mario.pos_y <= 49):
            self.frame = 0
            t = 0
        time.sleep(0.1)
        os.system("clear")
        sys.stdin.flush()
        for i in range(35):
            for j in range(0 + t, 100 + t):
                if(j < 1 + t or j > 98 + t):
                    stdout.write(Fore.WHITE + "X")
                elif(i == x - 3 and y == j and mario.st == 3):
                    stdout.write(Fore.WHITE + "*")
                elif(i == x - 2 and y == j and (mario.st == 2 or mario.st == 3)):
                    stdout.write(Fore.WHITE + "#")
                elif(i == x - 1 and y == j and mario.st == 1):
                    stdout.write(Fore.WHITE + "#")
                elif(i == x - 1 and y == j and (mario.st == 2 or mario.st == 3)):
                    stdout.write(Fore.GREEN + "I")
                elif(i == x and y == j):
                    stdout.write(Fore.GREEN + "I")
                else:
                    if(self.array[i][j] == "G"):
                        stdout.write(Fore.CYAN + self.array[i][j])
                    elif(self.array[i][j] == "!"):
                        stdout.write(Fore.RED + self.array[i][j])
                    elif(self.array[i][j] == "|"):
                        stdout.write(Fore.GREEN + self.array[i][j])
                    elif(self.array[i][j] == "O"):
                        stdout.write(Fore.WHITE + self.array[i][j])
                    elif(self.array[i][j] == "B"):
                        stdout.write(Fore.YELLOW + self.array[i][j])
                    elif(self.array[i][j] == "M"):
                        stdout.write(
                            Fore.BLUE + Style.BRIGHT + self.array[i][j])
                    elif(self.array[i][j] == "P"):
                        stdout.write(Fore.CYAN + self.array[i][j])
                    else:
                        stdout.write(Fore.YELLOW + self.array[i][j])
            stdout.write("\n")
        # deinit()
        print(
            Fore.WHITE +
            "score = ",
            mario.score,
            "|lives = ",
            mario.lives,
            "|timer = ",
            self.timer)
        sys.stdout.flush()

    def move_mario(self, mario, ch, cond, bullet):
        if(ch == 'd'):
            mario.pos_y += 1
            self.frame += 1
            if(not mario.is_ok(self)):
                if(self.array[mario.pos_x][mario.pos_y] == "*"):
                    mario.pos_y -= 1
                    mario.score += (30 - mario.pos_x) * 10
                    while(self.array[mario.pos_x + 1][mario.pos_y] == " "):
                        self.array[self.flag][287] = " "
                        self.flag += 1
                        self.array[self.flag][287] = "}"
                        mario.pos_x += 1
                        self.print_board(mario.pos_x, mario.pos_y, mario)
                    mario.level_done(self)

                mario.pos_y -= 1
                self.frame -= 1

                self.print_board(mario.pos_x, mario.pos_y, mario)
            else:
                if(self.array[mario.pos_x + 1][mario.pos_y] == ' ' and cond == 1):
                    timer = 6

                    self.jump_mario(mario, ch, timer, bullet)
                else:

                    self.print_board(mario.pos_x, mario.pos_y, mario)

        if(ch == 'a'):
            mario.pos_y -= 1
            #self.frame -= 1
            if(not mario.is_ok(self)):
                mario.pos_y += 1
                self.frame += 1

                self.print_board(mario.pos_x, mario.pos_y, mario)
            else:
                if(self.array[mario.pos_x + 1][mario.pos_y] == ' ' and cond == 1):
                    timer = 6
                    self.jump_mario(mario, ch, timer, bullet)
                else:

                    self.print_board(mario.pos_x, mario.pos_y, mario)

    def jump_mario(self, mario, ch, timer, bullet, cond=1):
        while(self.array[mario.pos_x + 1][mario.pos_y] == ' ' or cond == 1 or self.array[mario.pos_x + 1][mario.pos_y] == "G" or self.array[mario.pos_x + 1][mario.pos_y] == "!"):
            cond = 0
            check_t = 0
            if(timer > 6):
                if(mario.medium == 0):
                    mario.pos_x -= 1
                else:
                    mario.pos_x -= 2
                if(self.array[mario.pos_x - mario.st][mario.pos_y] != ' '):
                    next_piece = self.get_at(
                        mario.pos_x - mario.st, mario.pos_y)
                    obstacle = Obstacle()
                    if(obstacle.process(self, mario, next_piece, bullet) == "break"):
                        self.array[mario.pos_x - mario.st][mario.pos_y] = " "
                    else:
                        mario.pos_x += 1
                        timer = 13 - timer
                    self.print_board(mario.pos_x, mario.pos_y, mario)

                else:

                    self.print_board(mario.pos_x, mario.pos_y, mario)
            else:
                mario.pos_x += 1
                next_piece = self.get_at(mario.pos_x, mario.pos_y)
                if(next_piece != "!"):
                    mario.medium = 0
                if(self.array[mario.pos_x][mario.pos_y] != " "):
                    next_piece = self.get_at(mario.pos_x, mario.pos_y)

                    obstacle = Obstacle()
                    if(obstacle.process(self, mario, next_piece, bullet) != "kill"):
                        cond = 0
                        mario.pos_x -= 1
                    else:
                        for object in self.nature:
                            if(object.pos_x - 1 == mario.pos_x and object.pos_y == mario.pos_y):
                                object.on_hit(self, mario, bullet)
                        self.print_board(mario.pos_x, mario.pos_y, mario)
                else:
                    self.print_board(mario.pos_x, mario.pos_y, mario)
            ch = config.get_input()
            if(ch != 'w'):
                if(ch == 'f'):
                    bullet.spawn(mario, bd)
                else:
                    cond = 0
                    self.move_mario(mario, ch, cond, bullet)
            timer -= 1
        return

    def update_nature(self, mario):
        for object in self.nature:
            if(object.char == "#"):
                ref = object
            object.update(self, mario)
        for power in self.power:
            power.update(self, mario, ref)
        print("JAS")

    def get_at(self, pos_x, pos_y):
        return self.array[pos_x][pos_y]
