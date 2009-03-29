# -*- encoding: utf-8 -*-

import sys, string

M = 5
N = 4

PUZZLE = (
	(2, 1, 1, 3),
	(2, 1, 1, 3),
	(4, 5, 5, 6),
	(4, 7, 8, 6),
	(9, 0, 0, 10)
)

VISITED = {}

def is_visited(state):
	return state in VISITED

def is_solution(state):
	return state[14] == state[13] == state[18] == state[17] == "X"

def get_neighbor_cells(cell):
	result = []
	m,n = cell
	for rm in xrange(m-1, m+2):
		for rn in xrange(n-1, n+2):
			if rm >= 0 and rm < M and rn >= 0 and rn < N and (rm != m or rn != n):
				result.append((rm,rn))
	return result

def get_succ(state):
	result = []
	clear = []
	for m,row in enumerate(state):
		for n,part in enumerate(row):
			if part == 0:
				clear.append((m, n))
	print clear 
	return result

		
def print_state(state):
	n = 0
	for row in state:
		sys.stdout.write(str(row) + "\n")
			
if __name__ == '__main__':
	VISITED[PUZZLE] = True
	print_state(PUZZLE)
	for state in get_succ(PUZZLE):
		print "----"
		print_state(state)
	
