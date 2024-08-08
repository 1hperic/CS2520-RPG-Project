# map creation module

import pygame
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)


class TileMap:
	def __init__(self, tmx_file, tile_size=16):
		self.tmx_data = load_pygame(tmx_file)
		self.sprite_group = pygame.sprite.Group()
		self.tile_size = tile_size

		self.load_map()

	def load_map(self):
		# iterate through layers of map
		for layer in self.tmx_data.visible_layers:
			if hasattr(layer, 'data'):
				for x, y, surf in layer.tiles():
					if surf is None:
						continue
					pos = (x * self.tile_size, y * self.tile_size)
					Tile(pos=pos, surf=surf, groups=self.sprite_group)

	def draw(self, screen):
		# draw the tile sprites
		self.sprite_group.draw(screen)

	def get_layer(self, name):
		return self.tmx_data.get_layer_by_name(name)


def load_tilemap(tmx_file, tile_size=16):
	return TileMap(tmx_file, tile_size)
