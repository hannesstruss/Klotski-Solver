# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

import unittest

from klotski_solver import State, StateSuccessorFinder

class States(object):
	state1 = State((
		(1, 1, 0, 0),
		(1, 1, 0, 0),
		(0, 0, 0, 2),
		(0, 0, 0, 2),
		(0, 0, 0, 0),
	))
	
	state2 = State((
		(2, 2, 0, 0),
		(2, 2, 0, 0),
		(0, 0, 0, 1),
		(0, 0, 0, 1),
		(0, 0, 0, 0),
	))
	
	state3 = State((
		(2, 2, 0, 0),
		(2, 2, 0, 1),
		(0, 0, 0, 1), 
		(0, 0, 0, 0),
		(0, 0, 0, 0),
	))

class TestHashCodes(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_hash(self):
		self.assertEqual(hash(States.state1), hash(States.state2))
		self.assertNotEqual(hash(States.state1), hash(States.state3))
		self.assertNotEqual(hash(States.state2), hash(States.state3))

class TestStateSuccessors(unittest.TestCase):
	def test_successors(self):
		t = StateSuccessorFinder()
		
		
		
if __name__ == '__main__':
	unittest.main()