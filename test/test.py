import pygame
import sys

def run():
    pygame.init()
    screen = pygame.display.set_mode((1280,960))

    pygame.display.set_caption("Test!")

    while True:
        checkEvent()

        screen.fill((30, 30, 30))
        pygame.display.flip()

def checkEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
        print(event.type)

run()