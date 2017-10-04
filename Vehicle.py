class Vehicle(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, node):
        if self.x == node.x:
            pass
        elif self.x > node.x:
            self.x -= self.speed
        else:
            self.x += self.speed

        if self.y == node.y:
            pass
        elif self.y < node.y:
            self.y += self.speed
        else:
            self.y -= self.speed
