# -*- encoding: utf-8 -*-

import sys, string, time

from tools import curry
from Stack import Stack
from MyQueue import Queue

DIRECTIONS = ["t", "l", "r", "b"]

M = 5
N = 4
import puzzles

PUZZLE = puzzles.only_18

VISITED = {}

class State(object):
	def __init__(self, field):
		self.field = tuple(map(tuple, field))
		self.blocks = {}
		self.block_kinds = 0
		self.parent = None
		for m, row in enumerate(self.field):
			for n, content in enumerate(row):
				self.block_kinds = max(content, self.block_kinds)
				if content not in self.blocks:
					self.blocks[content] = []
				self.blocks[content].append((m, n))
	
	def __eq__(self, other):
		return self.field == other.field
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		return self.field.__hash__()
	
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
		
		for i in xrange(1, self.block_kinds + 1):
			directions = self.get_movable_directions_of_block(i)
			if directions:
				result.append((i, directions))
		return result
	
	def move_block(self, direction, content):
		cells = self.get_block_cells(content)
		result_cells = []
		state = map(list, self.field)
		
		for m,n in cells:
			if direction == "b":
				m_, n_ = m+1, n
			elif direction == "t":
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
		
def is_visited(state):
	return state in VISITED

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
	s = Queue(init_state)
	generated = 0
	outputted = 0
	current_time = time.time()
	solutions = []
	try:
		while s.count > 0:
			if generated - outputted > 10000:
				print generated
				tdiff = (time.time() - current_time) * 1000 / (generated - outputted)
				current_time = time.time()
				print "time per state: %sms" % tdiff
				outputted = generated
			node = s.pop()
			for child in node.get_succ():
				if child not in VISITED:
					VISITED[child] = True
					s.push(child)
					generated += 1
					if child.is_solution():
						solutions.append(child)
						print child
	except KeyboardInterrupt:
		print
		print "interrupted..."
	finally:
		print
		print "solutions:"
		for solution in solutions:
			print "depth", solution.get_depth()
			print solution
			print
			
			
		
if __name__ == '__main__':
	s = State(PUZZLE)
	print s
	print "..."
	walk_solutions(s)
