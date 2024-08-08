# battle module
import pygame

def start_battle(screen):
	# initialize battle variables
	player_hp = 5
	goblin_hp = 2
	turn = 'player'  # tracks current turn

	# font for rendering text
	font = pygame.font.Font(None, 36)

	# Load sprites
	player_sprite = pygame.image.load("assets/characters/stick_dude_still.png").convert_alpha()
	goblin_sprite = pygame.image.load("assets/characters/goblino.png").convert_alpha()
	player_sprite = pygame.transform.scale(player_sprite, (64, 64))
	goblin_sprite = pygame.transform.scale(goblin_sprite, (64, 64))

	def draw_battle_screen():
		screen.fill("white")
		# draw characters
		screen.blit(player_sprite, (50, screen.get_height() - 150))
		screen.blit(goblin_sprite, (screen.get_width() - 130, screen.get_height() - 150))
		
		# Display HP
		draw_text(f"Player HP: {player_hp}", font, "green" if player_hp > 2 else "red", 50, screen.get_height() - 100)
		draw_text(f"Goblino HP: {goblin_hp}", font, "green" if goblin_hp > 1 else "red", screen.get_width() - 180, screen.get_height() - 100)
		draw_text(f"Turn: {turn.capitalize()}", font, "blue", 50, screen.get_height() - 50)

	def draw_text(text, font, color, x, y):
		img = font.render(text, True, color)
		screen.blit(img, (x, y))

	# Battle loop
	battle_running = True
	while battle_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				battle_running = False

		# handle turn-based mechanics
		if turn == "player":
			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:	# player attacks
				goblin_hp -= 1
				if goblin_hp <= 0:
					goblin_hp = 0
					battle_running = False	# goblin defeated
				else:
					turn = "goblino"
		elif turn == "goblino":
			pygame.time.wait(1500)	# delay for goblin's turn (1.5 seconds)
			if goblin_hp > 0:
				player_hp -= 1
				if player_hp <= 0:
					player_hp = 0
					battle_running = False	# player defeated
				turn = "player"

		# Draw the battle screen
		draw_battle_screen()

		# update display
		pygame.display.flip()

		# cap framerate
		pygame.time.Clock().tick(60)

	# end battle
	return player_hp > 0	# return True if player wins, False if player loses; does not work currently
