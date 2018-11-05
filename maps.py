import config
from objects import Ghost


class map1:
    def __init__(self):
        self.width = 500
        self.height = 35
        self.array = []
        self.buff = []
        self.arr = []

    def init_map(self, bd):
        ghost1 = Ghost(bd, 30, 78, 5)
        ghost2 = Ghost(bd, 30, 123, 3)
        ghost3 = Ghost(bd, 30, 125, 3)
        ghost4 = Ghost(bd, 18, 260, 2)
        ghost5 = Ghost(bd, 30, 182, 1)
        ghost5 = Ghost(bd, 30, 180, 1)
        self.array = []
        for i in range(35):
            for j in range(500):
                self.buff.append(' ')
                if(i < 1 or i > 30 or j < 1 or j > 498):
                    self.buff[-1] = 'X'
                if(i > 30 and j > 104 and j < 109):
                    self.buff[-1] = ' '
                if((j > 70 and j < 73 and i > 27) or (i == 28 and j > 69 and j < 74)):
                    self.buff[-1] = 'X'
                if(j > 77 and j < 83 and i == 26):
                    if(j % 3 == 0):
                        self.buff[-1] = 'O'
                    elif(j % 3 == 1):
                        self.buff[-1] = 'M'
                    elif(j % 3 == 2):
                        self.buff[-1] = 'P'
                if((j == 86 or j == 87)and (i == 30 or i == 29)):
                    self.buff[-1] = "!"
                if(i == 19 and j > 88 and j < 95):
                    self.buff[-1] = "O"
                if(i == 15 and j > 88 and j < 95):
                    self.buff[-1] = "P"
                if(j > 112 and j < 118 and i > 29 - (j - 113)):
                    self.buff[-1] = "X"
                if(j > 130 and j < 138 and i >= 25 + (j - 130)):
                    self.buff[-1] = "X"
                if(j > 178 and j < 186 and i > 25 and i < 27):
                    if(j % 2 == 0):
                        self.buff[-1] = 'O'
                    elif(j % 2 == 1):
                        self.buff[-1] = 'P'
                if(j == 182 and i == 21):
                    self.buff[-1] = 'M'
                if((j > 220 and j < 223 and i > 27) or (i < 29 and i > 27 and j > 219 and j < 224)):
                    self.buff[-1] = 'X'
                if((j > 235 and j < 238 and i > 32) or (i < 29 and i > 27 and j > 234 and j < 239)):
                    self.buff[-1] = 'X'
                if((j == 256 or j == 257)and (i == 30 or i == 29)):
                    self.buff[-1] = "!"
                if(i == 19 and j > 258 and j < 267):
                    self.buff[-1] = "O"
                if(i == 18 and j == 259):
                    self.buff[-1] = "<"
                if(i == 18 and j == 266):
                    self.buff[-1] = ">"
                if(i == 13 and j > 258 and j < 267):
                    self.buff[-1] = "P"
                if(j > 269 and j < 277 and i > 29 - (j - 269)):
                    self.buff[-1] = "X"
                if(j == 286 and i > 17):
                    self.buff[-1] = "*"
                if(i == 18 and j == 287):
                    self.buff[-1] = "}"
                if(j == 306 and i < 30 and i > 25):
                    self.buff[-1] = "|"
                if(j == 305 and i == 29):
                    self.buff[-1] = "~"
                if(j == 304 and i == 30):
                    self.buff[-1] = "|"
                if(j == 306 and i == 30):
                    self.buff[-1] = "("
                if(j == 308 and i < 30 and i > 25):
                    self.buff[-1] = "|"
                if(j == 308 and i == 30):
                    self.buff[-1] = ")"
                if(j == 309 and i == 29):
                    self.buff[-1] = "~"
                if(j == 310 and i == 30):
                    self.buff[-1] = "|"
                if(j == 307 and i == 26):
                    self.buff[-1] = "~"

            self.array.append(self.buff)
            self.buff = []


class map2:
    def __init__(self):
        self.width = 500
        self.height = 35
        self.array = []
        self.buff = []
        self.arr = []

    def init_map(self, bd):
        ghost1 = Ghost(bd, 30, 78, 2)

        self.array = []
        for i in range(35):
            for j in range(500):
                self.buff.append(' ')
                if(i < 1 or i > 30 or j < 1 or j > 498):
                    self.buff[-1] = 'X'
                if(i > 30 and j > 104 and j < 109):
                    self.buff[-1] = ' '
                if((j > 70 and j < 73 and i > 27) or (i == 28 and j > 69 and j < 74)):
                    self.buff[-1] = 'X'
                if(j > 77 and j < 83 and i == 26):
                    if(j % 3 == 0):
                        self.buff[-1] = 'O'
                    elif(j % 3 == 1):
                        self.buff[-1] = 'M'
                    elif(j % 3 == 2):
                        self.buff[-1] = 'P'
                if((j == 86 or j == 87)and (i == 30 or i == 29)):
                    self.buff[-1] = "!"
                if(i == 19 and j > 88 and j < 95):
                    self.buff[-1] = "O"
                if(i == 15 and j > 88 and j < 95):
                    self.buff[-1] = "P"
                if(j > 112 and j < 118 and i > 29 - (j - 113)):
                    self.buff[-1] = "X"
                if(j >= 120 and j <= 124 and i == 25):
                    self.buff[-1] = "M"
                if(j > 130 and j < 138 and i >= 25 + (j - 130)):
                    self.buff[-1] = "X"
                if((j >= 163 and j <= 165) and(i <= 30 and i > 26)):
                    self.buff[-1] = "#"

            self.array.append(self.buff)
            self.buff = []
