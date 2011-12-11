# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

from collections import defaultdict
from operator import itemgetter

DIRECTIONS = ["u", "l", "r", "d"]
# rows/cols
M = 5
N = 4

class Solver(object):
	def __init__(self, puzzle):
		self.puzzle = puzzle
		
	def solve(self):
		pass
	
class StateSuccessorFinder(object):
	"""creates all possible subsequent states from a given initial state"""
	
	def __init__(self, state):
		self.state = state
	
	def get_block(self, cell):
		return self.state.field[cell[0]][cell[1]]
	
	def get_neighbor_cells(self, cell):
		"""return all the cells around the given one. Only consider directions up, right, down,
		   left, no diagonal
		"""
		fields = DIRECTIONS[:]
		result = {}
		m,n = cell
		for rm in xrange(m-1, m+2):
			for rn in xrange(n-1, n+2):
				if ((rm == m) ^ (rn == n)):
					field = fields[0]
					fields = fields[1:]
					if rm >= 0 and rm < self.state.rows and rn >= 0 and rn < self.state.cols:
						result[field] = (rm,rn)
					else:
						result[field] = None
		return result
	
	def get_movable_directions_of_block(self, block_id):
		"""return a set of directions in which the block with the given id could be moved"""
		directions = set(DIRECTIONS)
		cells = self.state.blocks[block_id]
		for cell in cells:
			for direction, neighbor in self.get_neighbor_cells(cell).iteritems():
				if neighbor is not None:
					neighbor_content = self.get_block(neighbor) 
					if neighbor_content != block_id and neighbor_content != 0 and direction in directions:
						directions.remove(direction)
				elif direction in directions: 
					directions.remove(direction)
		return directions
	
	def get_movable_blocks(self):
		"""return a set of block ids whose blocks are movable, paired with the directions
		   the block can be moved to
		"""
		result = set()
		for id in self.state.blocks.keys():
			for direction in self.get_movable_directions_of_block(id):
				result.add((id, direction))
		
		return result
	
	def move_block(self, block_id, direction):
		"""return a new state, with the block 'block_id' moved one step in 'direction'"""
		return None
	
	def get_successors(self):
		result = []
		
		for block_id in self.state.blocks:
			for direction in self.get_movable_directions_of_block(block_id):
				result.append(self.move_block(block_id, direction))
		
		return result
	
class State(object):
	"""A snapshot of a klotski board. Its field is a tuple of rows, which are tuples of cells.
	   Thus, cells are written as (row, col). It should be considered as immutable. All its 
	   methods are without side effects.
	"""
	def __init__(self, field):
		self.field = field
		self._blocks = None
		
	@property
	def rows(self):
		return len(self.field)
	
	@property
	def cols(self):
		return len(self.field[0])

	@property
	def blocks(self):
		"""return a list of sets of block cells. the list index is equal to the block id"""
		if self._blocks is None:
			self._blocks = defaultdict(lambda: set())
			for m in xrange(self.rows):
				for n in xrange(self.cols):
					content = self.field[m][n]
					if content != 0:
						self._blocks[content].add((m, n))
				
		return self._blocks

	def __eq__(self, other):
		return hash(self) == hash(other)

	def __neq__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		rslt = ""
		
		content_map = {}
		use_content = 0
		for row in self.field:
			for content in row:
				if content not in content_map:
					content_map[content] = use_content
					use_content += 1
				rslt += str(content_map[content])
		
		return rslt.__hash__()
	
