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
		