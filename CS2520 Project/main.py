import pygame
from config import *
from tilemap import *
from characters import *
from battle import start_battle  # import the battle function

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

# load map data
tile_map = TileMap("assets/maps/tutorial_cave.tmx")

# create character instances and locations
player = Player(100, 420)
goblino = Goblin(300, 50)

# main game loop
while running:
	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# update player
	keys = pygame.key.get_pressed()
	player.update(keys)

	# update goblino
	goblino.update()

	# check collision and start battle
	if pygame.sprite.collide_rect(player, goblino):
		# stop the main game loop
		running = False
		# start the battle
		battle_won = start_battle(screen)
		#if battle_won:
		#	print("Player won the battle!")
		#else:
		#	print("Player lost the battle.")

	# TODO: handle post-battle logic

	# draw everything
	screen.fill("white")  # fill the screen with white before drawing the map
	tile_map.draw(screen)
	player.draw(screen)
	goblino.draw(screen)

	# Update display
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()