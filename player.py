import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.image = pygame.Surface((32,64)) #Player's look
		self.image.fill('blue')
		self.rect = self.image.get_rect(topleft = pos)
		
		#Player movement
		self.direction = pygame.math.Vector2(0,0) #The first 0 is x, the second 0 is y.
		self.speed = 5
		self.gravity = 0.8
		self.jump_speed = -16 #It's negative because I need the player to jump UP.

	def import_character_assets(self):
		character_path = '.../character/'
		self.animations = {'idle':[],'run':[],'jump':[],'fall':[]} #A dictionary to save them.

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation]

	def get_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_a]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		if keys[pygame.K_w]:
			self.jump()

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jump_speed

	def update(self):
		self.get_input()