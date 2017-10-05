class Vehicle(object):

    def __init__(self, node):
        self.current_node = node

    def setPath(self, path):
        self.path = path

    def move(self):
        current_index = self.path.index[self.current_node]
        next_index = (current_index + 1) % len(self.path)
        self.current_node = self.path[current_index]