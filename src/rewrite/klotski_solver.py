# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

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
	
	def get_movable_directions_of_cell(self, cell):
		return set()
	
	def get_successors(self):
		return set()
	
class State(object):
	"""A snapshot of a klotski board. Its field is a tuple of rows, which are tuples of cells.
	   Thus, cells are written as (row, col)
	"""
	def __init__(self, field):
		self.field = field
		
	@property
	def rows(self):
		return len(self.field)
	
	@property
	def cols(self):
		return len(self.field[0])

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
	
