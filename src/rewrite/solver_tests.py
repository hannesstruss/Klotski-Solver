# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

import unittest

from klotski_solver import State, StateSuccessorFinder, M, N


class TestHashCodes(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_hash(self):
		self.assertEqual(hash(States.state1), hash(States.state2))
		self.assertNotEqual(hash(States.state1), hash(States.state2_succ1))
		self.assertNotEqual(hash(States.state2), hash(States.state2_succ1))

class TestStateEquality(unittest.TestCase):
	def test_equality(self):
		self.assertEqual(States.state1, States.state1) #identity
		
		self.assertEqual(States.state1, States.state2)
		self.assertEqual(States.state2, States.state1)
		
	def test_inequality(self):
		self.assertNotEqual(States.state0, States.state1)
		self.assertNotEqual(States.state1, States.state2_succ1)

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

class TestGetNeighborCells(unittest.TestCase):		
	def test_get_neighbor_cells(self):
		t = StateSuccessorFinder()
		
		self.assertEqual(t.get_neighbor_cells((0, 0)),
			{"u": None, "r": (0, 1), "d": (1, 0), "l": None})
		
		self.assertEqual(t.get_neighbor_cells((1, 0)),
			{"u": (0, 0), "r": (1, 1), "d": (2, 0), "l": None})
		
		self.assertEqual(t.get_neighbor_cells((M - 1, N - 1)),
			{"u": (M - 2, N - 1), "r": None, "d": None, "l": (M - 1, N - 2)})
		
		self.assertEqual(t.get_neighbor_cells((1, 2)),
			{"u": (0, 2), "r": (1, 3), "d": (2, 2), "l": (1, 1)})

class TestGetMovableDirectionsOfCell(unittest.TestCase):
	def test_get_movable_directions_of_cell(self):
		pass

class States(object):
	state0 = State((
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
	))
	
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
	
	state2_succ1 = State((
		(2, 2, 0, 0),
		(2, 2, 0, 1),
		(0, 0, 0, 1), 
		(0, 0, 0, 0),
		(0, 0, 0, 0),
	))
	
if __name__ == '__main__':
	unittest.main()