import random

class Pipe:
    def __init__(self,spawn_point):
        self.gap = None
        self.lower = None
        self.upper = None
        self.reset()
        self.x = 288 * 2 + spawn_point
        self.pointed = False
        self.cool_down = False
        self.width = 52
        self.height = 320

    def reset(self):
        self.gap = random.randint(45, 50)
        gap_y = random.randint(160, 350)
        self.upper = gap_y - self.gap -320
        self.lower = gap_y + self.gap
        self.pointed = False
        self.cool_down = False

    def update(self, rate):
        self.x -= rate

        if self.x <= -52:
            self.x = 288 * 2 - 50
            self.reset()

        return [self.x,self.lower, self.upper]
    def get_box(self,which):
        x1, x2 = self.x, self.x + self.width
        if which == "lower":
            y1, y2 = self.lower, 512
        else:
            y1, y2 = 0, self.upper+self.height
        return [x1,x2,y1,y2]