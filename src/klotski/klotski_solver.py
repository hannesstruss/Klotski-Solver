# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

from collections import defaultdict

DIRECTIONS = ["u", "l", "r", "d"]
DIRECTION_TUPLES = {
	"u": (-1, 0), "l": (0, -1), "r": (0, 1), "d": (1, 0),
}
# rows/cols
M = 5
N = 4

class Solver(object):
	def __init__(self, state):
		self.state = state
		
	def solve(self):
		finder = StateSuccessorFinder(None)
		visited = {}
		queue = [self.state]
		checked = 0
		result = None
		while len(queue) and not result:
			current = queue.pop()
			if current not in visited:
				mirrored = current.get_mirrored_state()
				checked += 1
				visited[current] = current
				visited[mirrored] = mirrored
				
				# TODO: find a better API for setting new states. This has a hacky smell.
				finder.state = current
				for successor in finder.get_successors():
					if successor.is_solution:
						result = successor
						break
					else:
						queue.insert(0, successor)
		#print "Ende:", checked
		return result

class SolutionPrinter(object):
	# TODO: if two consecutive steps move the same block in the same direction, count them as one
	def print_solution(self, state):
		# use an array, because Python 2.x doesn't have nonlocal
		index = [-1]
		def str_index(s):
			index[0] += 1
			return "%s: %s" % (index[0], s)
		
		steps = [state]
		parent = state.parent
		while parent is not None:
			steps.append(parent)
			parent = parent.parent
		print "\n".join(map(str_index, steps[::-1]))
	
class StateSuccessorFinder(object):
	"""creates all possible subsequent states from a given initial state. Not thread-safe"""
	
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
		"""return a new state, with the block 'block_id' moved one step in 'direction'
		   Requires that the block is actually movable
		"""
		
		rows = []
		
		for row_nr in xrange(self.state.rows):
			row = []
			for col_nr in xrange(self.state.cols):
				row.append(self.state.field[row_nr][col_nr])
			rows.append(row)
			
		for cell in self.state.blocks[block_id]:
			rows[cell[0]][cell[1]] = 0
			
		for cell in self.state.blocks[block_id]:
			moved_cell = cell[0] + DIRECTION_TUPLES[direction][0], cell[1] + DIRECTION_TUPLES[direction][1]
			rows[moved_cell[0]][moved_cell[1]] = block_id
				
		result = State(tuple(map(tuple, rows)))
		
		result.parent = self.state
		return result
	
	def get_successors(self):
		result = set()
		
		for block_id in self.state.blocks:
			for direction in self.get_movable_directions_of_block(block_id):
				result.add(self.move_block(block_id, direction))
		
		return result
	
class State(object):
	"""A snapshot of a klotski board. Its field is a tuple of rows, which are tuples of cells.
	   Thus, cell tuples are in the form of (row, col). It should be considered as immutable. All its 
	   methods are without side effects.
	"""
	def __init__(self, field):
		self.field = field
		self.parent = None
		self._blocks = None
		
	@property
	def rows(self):
		return len(self.field)
	
	@property
	def cols(self):
		return len(self.field[0])

	@property
	def blocks(self):
		"""returns a dictionary which maps block ids to a set of cells"""
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

	def __repr__(self):
		return "\nState(\n%s)\n" % ("\n".join(map(str, self.field)),)

	def get_mirrored_state(self):
		"""returns a state whose field equals this one's, mirrored horizontally"""
		rows = []
		for row in self.field:
			rows.append(row[::-1])
		return State(tuple(rows))

	@property
	def is_solution(self):
		# TODO: this doesn't work for arbitrary widths/heights
		return self.field[4][1] == self.field[4][2] == 1

	def get_block_cells(self):
		blocks = []
		for cell_set in self.blocks.values():
			blocks.append(frozenset(cell_set))
		return frozenset(blocks)

	def __hash__(self):
		return hash(self.get_block_cells())
	
if __name__ == '__main__':
	print "SOLVING!"
	import puzzles
	printer = SolutionPrinter()
	solver = Solver(State(puzzles.red_donkey))
	
	result = solver.solve()
	printer.print_solution(result)