import sys, pygame
from Node import *
from Vehicle import *

pygame.init()

size = width, height = 300,300

screen = pygame.display.set_mode()
pygame.display.toggle_fullscreen()

surface = pygame.display.get_surface()
black = 0,0,0
screen.fill(black)
lineColor = 120,120,10
lastPos = 0,0

nodes = []
nodes.append(Node(10,10))
nodes.append(Node(100,10))
nodes.append(Node(50,50))
nodes[0].add(nodes[1])
nodes[1].add(nodes[2])


car = Vehicle(10, 10, 5)
target = 1

black = 0,0,0
while 1:
    surface.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.line(surface, lineColor, lastPos, pygame.mouse.get_pos(), 4)
            lastPos = pygame.mouse.get_pos()

    for n in nodes:
        pygame.draw.circle(surface, lineColor, n.getPos(), 20, 4)

    for n in nodes:
        for c in n.matrix:
            if len(c) > 0:
                pygame.draw.line(surface, lineColor, n.getPos(), c[0].getPos(), 4)

    if time.time() - t > 0.1:
        if car.x == nodes[target].getPos()[0] and car.y == nodes[target].getPos()[1]:
            target = 2
        car.move(nodes[target])
        t = time.time()
    pygame.draw.circle(surface, lineColor, (car.x,car.y), 40, 4)

    pygame.display.flip()
