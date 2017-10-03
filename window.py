class Node(object):

    def __init__(self,x,y):
        self.matrix = []
        self.x = x
        self.y = y

    def getPos(self):
        return self.x, self.y

    def add(self, node):
        self.matrix.append([node])

    def get_row(self, node):
        for x in self.matrix:
            if node in x:
                return x

    def add_constrain(self, node, constrain):
        if constrain not in Node.get_row(self, node):
            self.get_row(node).append(constrain)

    def is_satisfied(self, node):
        for x in self.get_row(node):
            if isinstance(x, Constraint):
                if not x.is_satisfied():
                    return False
        return True

""" 
    holder for functions and variables for boolean logic
"""
class Constraint(object):

    def __init__(self):
        self.constraints = []

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def is_satisfied(self):
        for x in self.constraints:
            if callable(x):
                if not x(self):
                    return False
            else:
                if not x:
                    return False
        return True

    def green_light(self):
        return True
