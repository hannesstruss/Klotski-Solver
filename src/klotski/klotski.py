# -*- encoding: utf-8 -*-

import sys, string

from tools import curry

M = 5
N = 4

PUZZLE = (
	(2, 1, 1, 3),
	(2, 1, 1, 3),
	(4, 5, 5, 6),
	(4, 7, 8, 6),
	(9, 0, 0, 10)
)

# easy debug puzzle
PUZZLE = (
	(4, 5, 5, 6),
	(4, 7, 8, 6),
	(2, 1, 1, 3),
	(2, 1, 1, 3),
	(9, 0, 0, 10)
)


VISITED = {}

class State(object):
	def __init__(self, field):
		self.field = field
	
	def __eq__(self, other):
		return self.field == other.field
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		return self.field.__hash__()
	
	def is_solution(self):
		return self.field[3][1] == self.field[3][2] == self.field[4][1] == self.field[4][2] == 1
	
	def get_cell_content(self, cell):
		m,n = cell
		return self.field[m][n]
	
	def get_block_cells(self, content):
		"""return all cells whose content is 'content'"""
		result = []
		for m,row in enumerate(self.field):
			for n,cell_content in enumerate(row):
				if cell_content == content:
					result.append((m,n))
		return result
	
	def get_succ(self):
		result = []
		clear = []
		for m,row in enumerate(self.field):
			for n,part in enumerate(row):
				if part == 0:
					clear.append((m, n))
		
		for clear_cell in clear:
			print clear_cell, get_neighbor_cells(clear_cell)
				
		
		return result
		
def is_visited(state):
	return state in VISITED

def get_neighbor_cells(cell):
	fields = ["t", "l", "r", "b"]
	result = {}
	m,n = cell
	for rm in xrange(m-1, m+2):
		for rn in xrange(n-1, n+2):
			if ((rm == m) ^ (rn == n)):
				field = fields[0]
				fields = fields[1:]
				if rm >= 0 and rm < M and rn >= 0 and rn < N:
					result[field] = (rm,rn)
	return result

		
def print_state(state):
	n = 0
	print "\n".join(map(str, state.field))
			
if __name__ == '__main__':
	s = State(PUZZLE)
	
	VISITED[s] = True
	print_state(s)
	for state in s.get_succ():
		print "----"
		print_state(state)
	
