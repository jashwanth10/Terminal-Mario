import config
from board import Board
from objects import Ghost
import time
import os
import sys
from players import Mario
from config import nature
from powers import bullets


def main():
    print("Use 'w' for Jump")
    print("Use 'd' to move right")
    print("Use 'a' to move left")
    print("Choose Level:\nAvailable Options: 1,2")
    level = input()
    sys.stdin.flush()
    while(level != "1" and level != "2"):
        print("Choose valid Level:")
        level = input()
    os.system("clear")
    print("\t\t\t\tINITIALIZING:")
    time.sleep(1)
    mario = Mario()
    bd = Board(level)
    bd.init_board()
    bullet = bullets(mario, bd)

    # nature.append(ghost1)
    frame_no = bd.frame
    while(frame_no < 395):
        ch = config.get_input()
        if(ch == 'a' or ch == 'd'):
            bd.move_mario(mario, ch, 1, bullet)
        elif(ch == 'f'):
            if(mario.st == 3):
                bullet.spawn(mario, bd)
        elif(ch == 'w'):
            timer = 12
            bd.jump_mario(mario, ch, timer, bullet)
        if(ch == 'z'):
            exit()

        bd.print_board(mario.pos_x, mario.pos_y, mario)


main()
