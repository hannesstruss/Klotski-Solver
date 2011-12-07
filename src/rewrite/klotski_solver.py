# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

class Solver(object):
	def __init__(self, puzzle):
		self.puzzle = puzzle
		
	def solve(self):
		pass

class State(object):
	def __init__(self, field):
		self.field = field
		
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
	
