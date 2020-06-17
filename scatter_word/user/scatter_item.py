import numpy as np
import math

class scatter_item():
    def __init__(self, nums, board_x_up, board_y_up, board_x_l, board_y_l,):
        self.nums = nums
        self.board_x_up = board_x_up
        self.board_y_up = board_y_up
        self.board_x_l = board_x_l
        self.board_y_l = board_y_l
        self.on_postion = 0
        self.x = np.random.randint(-200, 201, nums)
        self.y = np.random.randint(-100, 101, nums)
        self.direction_x = np.random.choice([-1, 1], nums)
        self.direction_y = np.random.choice([-1, 1], nums)
        self.speed = np.random.randint(3, 6, nums)
        self.scatter_size = np.random.randint(200, 500, nums)
        self.line_and_taken = []

    def on_board_or_not(self):
        for i in range(self.nums):
            if((self.x[i] > self.board_x_up) or (self.x[i] < self.board_x_l)):
                self.direction_x[i] = - self.direction_x[i]
                if (self.x[i] > self.board_x_up): self.x[i] -= 3 # 解决卡墙bug
                if (self.x[i] < self.board_x_up): self.x[i] += 3 # 解决卡墙bug
            if((self.y[i] > self.board_y_up) or (self.y[i] < self.board_y_l)):
                self.direction_y[i] = - self.direction_y[i]
                if (self.y[i] > self.board_y_up): self.y[i] -= 3 # 解决卡墙bug
                if (self.y[i] < self.board_y_up): self.y[i] += 3 # 解决卡墙bug

            # if(self.speed[i] != 0 and (self.x[i] >= self.board_x_up or
            # self.y[i] >= self.board_y_up or self.x[i] <= self.board_x_l or self.y[i] <= self.board_y_l)):

    def move_scatter(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

    def spread(self, level=0):
        if level == 0:
            self.speed = np.random.randint(3, 6, self.nums)
        if level == 1:
            self.speed = np.random.randint(4, 7, self.nums)
        if level == 2:
            self.speed = np.random.randint(5, 8, self.nums)
        if level == 3:
            self.speed = np.random.randint(6, 9, self.nums)
        if level == 4:
            self.speed = np.random.randint(7, 10, self.nums)


    def on_word_or_not(self, word_shape_line):
        for i in range(self.nums):
            x = int(self.x[i]*0.25 + 50)
            y = int(self.y[i]*(-0.25) + 25)
            line = 100 * y + x

            # line_w1 = line + 1
            # line_sw1 = line + 100 + 1
            # line_s1 = line + 100
            # line_se1 = line + 100 - 1
            # line_e1 = line - 1
            # line_ne1 = line - 100 - 1
            # line_n1 = line - 100
            # line_nw1 = line - 100 + 1

            if(line in word_shape_line and line not in self.line_and_taken):
                self.speed[i] = 0
                self.line_and_taken.append(line)
                # self.line_and_taken.append(line_w1)
                # self.line_and_taken.append(line_sw1)
                # self.line_and_taken.append(line_s1)
                # self.line_and_taken.append(line_se1)
                # self.line_and_taken.append(line_e1)
                # self.line_and_taken.append(line_ne1)
                # self.line_and_taken.append(line_n1)
                # self.line_and_taken.append(line_nw1)

