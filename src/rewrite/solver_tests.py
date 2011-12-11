# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

import unittest

from klotski_solver import State, StateSuccessorFinder, M, N

# Tests for State
class TestHashCodes(unittest.TestCase):
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
		
class TestGetBlocks(unittest.TestCase):
	def clone_state(self, state):
		return State(state.field)
	
	def test_get_blocks(self):
		state = self.clone_state(States.state0)
		self.assertEqual(state.get_blocks(), {})
		
		state = self.clone_state(States.state1)
		self.assertEqual(state.get_blocks(), {
			1: set([(0, 0), (0, 1), (1, 0), (1, 1)]),
			2: set([(2, 3), (3, 3)]),
		})
		
		state = self.clone_state(States.state4)
		self.assertEqual(state.get_blocks(), {
			1: set([(0, 0)]),
			2: set([(0, 1)]),
			3: set([(1, 1)]),
			4: set([(1, 0)]),
		})

# Tests for StateSuccessorFinder
class TestStateSuccessors(unittest.TestCase):
	def test_successors_count(self):
		succs = StateSuccessorFinder(States.state1).get_successors()
		self.assertEqual(len(succs), 5)
		
	def test_successors_correctness(self):
		succs = StateSuccessorFinder(States.state1).get_successors()
		self.assertEqual(
			set([States.state1_succ1, States.state1_succ2, States.state1_succ3, 
			     States.state1_succ4, States.state1_succ5]),
			succs
		)

class TestGetNeighborCells(unittest.TestCase):		
	def test_get_neighbor_cells(self):
		t = StateSuccessorFinder(States.state0)
		
		self.assertEqual(t.get_neighbor_cells((0, 0)),
			{"u": None, "r": (0, 1), "d": (1, 0), "l": None})
		
		self.assertEqual(t.get_neighbor_cells((1, 0)),
			{"u": (0, 0), "r": (1, 1), "d": (2, 0), "l": None})
		
		self.assertEqual(t.get_neighbor_cells((M - 1, N - 1)),
			{"u": (M - 2, N - 1), "r": None, "d": None, "l": (M - 1, N - 2)})
		
		self.assertEqual(t.get_neighbor_cells((1, 2)),
			{"u": (0, 2), "r": (1, 3), "d": (2, 2), "l": (1, 1)})

class TestGetMovableDirectionsOfBlock(unittest.TestCase):
	def test_get_movable_directions_of_block(self):
		t = StateSuccessorFinder(States.state1)
		self.assertEqual(t.get_movable_directions_of_block((0, 0)),
			set(["r", "d"]))
		
		self.assertEqual(t.get_movable_directions_of_block((2, 3)),
			set(["l", "u", "d"]))
		
		t = StateSuccessorFinder(States.state3)
		self.assertEqual(t.get_movable_directions_of_block((2, 1)),
			set(["u", "r", "d", "l"]))

class TestGetMovableBlocks(unittest.TestCase):
	def test_get_movable_blocks(self):
		t = StateSuccessorFinder(States.state0)
		self.assertEqual(t.get_movable_blocks(), set())
		
		t = StateSuccessorFinder(States.state1)
		self.assertEqual(t.get_movable_blocks(), set([
			(1, "r"),
			(1, "d"),
			(2, "u"),
			(2, "l"),
			(2, "d"),
		]))
		
		t = StateSuccessorFinder(States.state4)
		self.assertEqual(t.get_movable_blocks(), set([
			(4, "d"),
			(3, "d"),
			(3, "r"),
			(2, "r"),
		]))

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
	
	state3 = State((
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 1, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
	))
	
	state4 = State((
		(1, 2, 0, 0),
		(4, 3, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
	))
	
if __name__ == '__main__':
	unittest.main()