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
	
	state1_succ1 = State((
		(0, 1, 1, 0),
		(0, 1, 1, 0),
		(0, 0, 0, 2),
		(0, 0, 0, 2),
		(0, 0, 0, 0),
	))
	
	state1_succ2 = State((
		(0, 0, 0, 0),
		(1, 1, 0, 0),
		(1, 1, 0, 2),
		(0, 0, 0, 2),
		(0, 0, 0, 0),
	))
	
	state1_succ3 = State((
		(1, 1, 0, 0),
		(1, 1, 0, 2),
		(0, 0, 0, 2),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
	))
	
	state1_succ4 = State((
		(1, 1, 0, 0),
		(1, 1, 0, 0),
		(0, 0, 2, 0),
		(0, 0, 2, 0),
		(0, 0, 0, 0),
	))
	
	state1_succ5 = State((
		(1, 1, 0, 0),
		(1, 1, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 2),
		(0, 0, 0, 2),
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
	def setUp(self):
		self.t = StateSuccessorFinder()
		
	def test_successors_count(self):
		succs = self.t.get_successors(States.state1)
		self.assertEqual(len(succs), 5)
		
	def test_successors_correctness(self):
		succs = self.t.get_successors(States.state1)
		self.assertEqual(
			set([States.state1_succ1, States.state1_succ2, States.state1_succ3, 
			     States.state1_succ4, States.state1_succ5]),
			succs
		)
		
		
if __name__ == '__main__':
	unittest.main()