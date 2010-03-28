# -*- encoding: utf-8 -*-
import sys, string, time

from tools import curry
from Stack import Stack
from MyQueue import Queue
import puzzles

DIRECTIONS = ["u", "l", "r", "d"]

# dont change, code isn't completely dynamic yet
M = 5
N = 4

class State(object):
	def __init__(self, field):
		self.field = tuple(map(tuple, field))
		self.blocks = {}
		self.parent = None
		for m, row in enumerate(self.field):
			for n, cell_content in enumerate(row):
				if cell_content == 0:
					continue
				if cell_content not in self.blocks:
					self.blocks[cell_content] = []
				self.blocks[cell_content].append((m, n))
	
	def __eq__(self, other):
		return hash(other) == hash(self)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		rslt = ""
		
		content_map = {}
		use_content = 0
		for m, row in enumerate(self.field):
			for n, content in enumerate(row):
				if content not in content_map:
					content_map[content] = use_content
					use_content += 1
				rslt += str(content_map[content])
		
		return rslt.__hash__()
	
	def __str__(self):
		return "\n".join(map(str, self.field))
	
	def is_solution(self):
		return self.field[3][1] == self.field[3][2] == self.field[4][1] == self.field[4][2] == 1
	
	def get_cell_content(self, cell):
		m,n = cell
		return self.field[m][n]
	
	def get_block_cells(self, content):
		"""return all cells whose content is 'content'"""
		return self.blocks.get(content, [])[:]
	
	def get_depth(self):
		depth = 1
		parent = self.parent
		while parent is not None:
			depth += 1
			parent = parent.parent
		return depth
	
	def get_movable_directions_of_block(self, content):
		directions = set(DIRECTIONS)
		for cell in self.get_block_cells(content):
			directions = directions & self.get_movable_directions_of_cell(cell)
		return directions
	
	def get_movable_directions_of_cell(self, cell):
		"""return a set of directions in which 'cell' could be moved"""
		directions = set(DIRECTIONS)
		cell_content = self.get_cell_content(cell)
		for direction, neighbor in get_neighbor_cells(cell).iteritems():
			if neighbor is not None:
				neighbor_content = self.get_cell_content(neighbor) 
				if not (neighbor_content == cell_content or neighbor_content == 0):
					directions.remove(direction)
			else: 
				directions.remove(direction)
		return directions
	
	def get_movable_blocks(self):
		result = []
		
		for i in xrange(1, len(self.blocks) + 1):
			directions = self.get_movable_directions_of_block(i)
			if directions:
				result.append((i, directions))
		return result
	
	def move_block(self, direction, content):
		cells = self.get_block_cells(content)
		result_cells = []
		state = map(list, self.field)
		
		for m,n in cells:
			if direction == "d":
				m_, n_ = m+1, n
			elif direction == "u":
				m_, n_ = m-1, n
			elif direction == "l":
				m_, n_ = m, n-1
			elif direction == "r":
				m_, n_ = m, n+1
			
			result_cells.append((m_, n_))
			state[m_][n_] = content
				
		for m,n in set(cells) - set(result_cells):
			state[m][n] = 0
		
		return State(state)
		
				
	def get_succ(self):
		result = []
				
		movable_blocks = self.get_movable_blocks()
		for content,directions in movable_blocks:
			for direction in directions:
				result_state = self.move_block(direction, content)
				result_state.parent = self
				result.append(result_state)
		
		return result
	
	def get_ancestors_num(self):
		result = 0
		s = self
		while s.parent is not None:
			result += 1
			s = s.parent
		return result
	
	def get_ancestry_str(self):
		result = ""
		s = self
		while s is not None:
			result += str(s) + "\n\n"
			s = s.parent
		return result
		
		
def get_neighbor_cells(cell):
	fields = DIRECTIONS[:]
	result = {}
	m,n = cell
	for rm in xrange(m-1, m+2):
		for rn in xrange(n-1, n+2):
			if ((rm == m) ^ (rn == n)):
				field = fields[0]
				fields = fields[1:]
				if rm >= 0 and rm < M and rn >= 0 and rn < N:
					result[field] = (rm,rn)
				else:
					result[field] = None
	return result

def walk_solutions(init_state):
	s = Stack(init_state)
	visited = set()
	solutions = []
	try:
		while len(s) > 0:
			state = s.pop()
			if state.is_solution():
				solutions.append(state)
				print "solutions:", len(solutions)
			else:
				for succ in state.get_succ():
					if succ not in visited:
						s.push(succ)
			visited.add(state)
				
	except KeyboardInterrupt:
		print "interrupted"
		
	for solution in solutions:
		print "#####################"
		print solution.get_ancestors_num()
		print solution.get_ancestry_str()
		print "#####################\n\n"
	
	print "visited:", len(visited)
		
	
def test_if_states_are_equivalent(state1, state2):
	pass
			
		
if __name__ == '__main__':
	s = State(puzzles.only_18)
	walk_solutions(s)
