# animation module

import pygame

class Animation:
	def __init__(self, spritesheet_path, frame_width, frame_height, num_frames, frame_rate):
		self.spritesheet = pygame.image.load(spritesheet_path).convert_alpha()
		self.frame_width = frame_width
		self.frame_height = frame_height
		self.num_frames = num_frames
		self.frame_rate = frame_rate
		self.frames = self.load_frames()
		self.current_frame = 0
		self.frame_timer = 0

	def load_frames(self):
		frames = []
		for i in range(self.num_frames):
			frame = self.spritesheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height))
			frames.append(frame)
		return frames

	def update(self):
		self.frame_timer += 1
		if self.frame_timer >= self.frame_rate:
			self.frame_timer = 0
			self.current_frame += 1
			if self.current_frame >= len(self.frames):
				self.current_frame = 0

	def get_current_frame(self):
		return self.frames[self.current_frame]

	def reset(self):
		self.current_frame = 0
		self.frame_timer = 0

