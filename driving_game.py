import pygame
from pygame.locals import *

pygame.init()
running = True
size = width, height = (1200, 800)
road_width = int(width / 2)
road_mark_width = int(width / 60)
road_dash_height = 30
dash_gap = 20
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Driving Game')
screen.fill((100, 255, 80))

# draw road
pygame.draw.rect(
    screen,
    (50, 50, 50),
    (width / 2-road_width / 2, 0, road_width, height))

# draw centre marking
y = 0
while y < height:
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_mark_width / 2, y, road_mark_width, road_dash_height)) 
    y += road_dash_height + dash_gap

#draw left marking
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width / 2 - road_width + road_mark_width * 16, 0, road_mark_width, height))

#draw right marking
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width / 2 + road_width - road_mark_width * 17, 0, road_mark_width, height))

pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()



class Player:

    def __init__(self):
        self.x = width / 2
        self.y = height / 2
    