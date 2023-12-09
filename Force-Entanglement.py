import pygame
from settings import *
from level import Level

pygame.display.set_caption("Force: Entanglement")
#Init
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_hitbox,screen)

#Game loop
run = True
while run:
	#Check if stop game loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill('black')
	level.run()
	
	pygame.display.update()
	clock.tick(60)
pygame.quit()