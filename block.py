from colors import Colors
import pygame


class Block:
	def __init__(self, id):
		self.id = id
		self.cells = {}
		self.cell_size = 30
		self.row_offset = 0
		self.column_offset = 0
		self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns
    
    def draw(self, screen):
        tiles = self.get_cell_positions()
		for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)