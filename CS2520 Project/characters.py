# character creation module

import pygame
from config import *
from animation import Animation

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, image_path="assets/characters/stick_dude.png"):
		super().__init__()
		self.animation = Animation(image_path, 24, 24, 3, 10)  # adjust dimensions and frame rate as needed
		self.rect = pygame.Rect(x, y, 24, 24)  # match frame dimensions
		self.speed = 2
		self.moving = False

	# character movement
	def update(self, keys):
		self.moving = False
		if keys[pygame.K_a]:
			self.rect.x -= self.speed
			self.moving = True
		if keys[pygame.K_d]:
			self.rect.x += self.speed
			self.moving = True
		if keys[pygame.K_w]:
			self.rect.y -= self.speed
			self.moving = True
		if keys[pygame.K_s]:
			self.rect.y += self.speed
			self.moving = True

		# ensure player stays within screen bounds
		self.rect.x = max(0, min(self.rect.x, WINDOW_WIDTH - self.rect.width))
		self.rect.y = max(0, min(self.rect.y, WINDOW_HEIGHT - self.rect.height))

		# update animation when moving
		if self.moving:
			self.animation.update()
		else:
			self.animation.reset()

	def draw(self, surface):
		frame = self.animation.get_current_frame()
		surface.blit(frame, self.rect)

	def handle_collision(self, other_sprite):
		# temporary variables for calculating exact collision
		temp_rect = self.rect.copy()

		# horizontal collision
		if self.rect.colliderect(other_sprite.rect):
		# determine horizontal collision side
			if temp_rect.right > other_sprite.rect.left and temp_rect.left < other_sprite.rect.left:
				# Colliding from the left
				self.rect.right = other_sprite.rect.left
			elif temp_rect.left < other_sprite.rect.right and temp_rect.right > other_sprite.rect.right:
				# Colliding from the right
				self.rect.left = other_sprite.rect.right

		# recalculate temp rect after horizontal correction
			temp_rect = self.rect.copy()

		# vertical collision
		if temp_rect.colliderect(other_sprite.rect):
			if temp_rect.bottom > other_sprite.rect.top and temp_rect.top < other_sprite.rect.top:
				# colliding from above
				self.rect.bottom = other_sprite.rect.top
			elif temp_rect.top < other_sprite.rect.bottom and temp_rect.bottom > other_sprite.rect.bottom:
				# colliding from below
				self.rect.top = other_sprite.rect.bottom

class Goblin(pygame.sprite.Sprite):
	def __init__(self, x, y, image_path="assets/characters/goblino.png"):
		super().__init__()
		self.image = pygame.image.load(image_path).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self, surface):
		surface.blit(self.image, self.rect)