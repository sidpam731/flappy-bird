class Player:
    def __init__(self,vol,y_lvl,x,adder,chars,health):
        self.vol = vol
        self.y_lvl = y_lvl
        self.x = x
        self.adder = adder
        self.chars = chars
        self.health = health
        self.is_touching = False
        self.points = 0
    def update(self,is_up):
        if is_up and self.y_lvl > 12:
            if self.y_lvl > 24:
                self.y_lvl -= self.adder
                char = self.chars.up
            else:
                char = self.chars.mid

        else:
            if int(self.y_lvl)-2 < 512-(24+112):
                self.y_lvl += self.vol/2
                char = self.chars.down
            else:
                char = self.chars.mid
                self.is_touching = True
        data = [char,self.y_lvl,self.x]
        return data
    def get_box(self):
        x1,x2 = self.x,self.x+17
        y1, y2 = self.y_lvl, self.y_lvl + 12
        return [x1,x2,y1,y2]

