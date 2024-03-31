from grid import Grid
from blocks import *
import random


class Game:
	def __init__(self):
		self.grid = Grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

    def get_random_block(self):
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block