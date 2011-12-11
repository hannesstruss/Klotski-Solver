from operator import attrgetter

import unittest

from klotski import State
from MyQueue import Queue

class Fields(object):
	trivial = (
		(0, 1, 1, 0),
		(0, 1, 1, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	trivial_alt = (
		(0, 2, 2, 0),
		(0, 2, 2, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	trivial2 = (
		(1, 1, 0, 0),
		(1, 1, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	trivial3 = (
		(0, 0, 1, 1),
		(0, 0, 1, 1),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	trivial5 = (
		(0, 0, 0, 0),
		(0, 1, 1, 0),
		(0, 1, 1, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	trivial4 = (
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 1, 1),
		(0, 0, 1, 1)
	)
	
	blocked1 = (
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 2),
		(0, 0, 1, 1),
		(0, 3, 1, 1)
	)
	
	blocked2 = (
		(1, 1, 1, 1),
		(1, 1, 1, 1),
		(1, 1, 1, 1),
		(1, 1, 1, 1),
		(1, 1, 1, 1),
	)
	
	neighbors = (
		(1, 1, 2, 2),
		(1, 1, 2, 2),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	neighbors_alt = (
		(2, 2, 1, 1),
		(2, 2, 1, 1),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	neighbors2 = (
		(0, 0, 2, 2),
		(1, 1, 2, 2),
		(1, 1, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	neighbors3 = (
		(1, 1, 0, 0),
		(1, 1, 2, 2),
		(0, 0, 2, 2),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	)
	
	equi = (
		(1, 0, 2, 3),
		(1, 4, 2, 0),
		(1, 4, 5, 5),
		(0, 0, 5, 5),
		(6, 6, 0, 0)
	)
	
	equi_alt = (
		(6, 0, 3, 2),
		(6, 5, 3, 0),
		(6, 5, 4, 4),
		(0, 0, 4, 4),
		(1, 1, 0, 0)
	)
	
	only_18_equi1 = (
		(2, 1, 1, 3),
		(4, 1, 1, 5),
		(6, 7, 8, 9),
		(10, 0, 0, 13),
		(14, 11, 12, 15)
	)
	
	only_18_equi2 = (
		(2, 1, 1, 3),
		(4, 1, 1, 5),
		(6, 7, 8, 9),
		(10, 0, 0, 13),
		(14, 11, 12, 15)
	)

class TestState(unittest.TestCase):
	def test_init(self):
		s = State(Fields.trivial)
		self.assertEqual(len(s._blocks), 1)
		self.assertEqual(s.field, Fields.trivial)
		
		s = State(Fields.blocked1)
		self.assertEqual(len(s._blocks), 3)
		
		s = State(Fields.blocked2)
		self.assertEqual(len(s._blocks), 1)
		
	def test_get_movable_directions_of_block(self):
		s = State(Fields.trivial)
		self.assertEqual(s.get_movable_directions_of_block(1), set(["r", "l", "d"]))
		
		s = State(Fields.trivial2) 
		self.assertEqual(s.get_movable_directions_of_block(1), set(["r", "d"]))
		
		s = State(Fields.trivial3) 
		self.assertEqual(s.get_movable_directions_of_block(1), set(["l", "d"]))
		
		s = State(Fields.trivial4) 
		self.assertEqual(s.get_movable_directions_of_block(1), set(["l", "u"]))
		
		s = State(Fields.blocked1)
		self.assertEqual(s.get_movable_directions_of_block(1), set([]))
		
		s = State(Fields.blocked2)
		self.assertEqual(s.get_movable_directions_of_block(1), set([]))
		
	def test_get_succ(self):
		s = State(Fields.trivial)
		succ_fields = set(map(attrgetter("field"), s.get_succ()))
		self.assertEqual(succ_fields,
			set([Fields.trivial2, Fields.trivial3, Fields.trivial5]))
		
		s = State(Fields.neighbors)
		succ_fields = set(map(attrgetter("field"), s.get_succ()))
		self.assertEqual(succ_fields,
			set([Fields.neighbors2, Fields.neighbors3]))
		
	def test_hash_and_equality(self):
		s = State(Fields.trivial)
		s2 = State(Fields.trivial)
		self.assertEqual(s, s2)
		
		s3 = State(Fields.trivial2)
		self.assertNotEqual(s, s3)
		
		s4 = State(Fields.trivial_alt)
		self.assertEqual(s, s4)
		
		s5 = State(Fields.neighbors)
		s6 = State(Fields.neighbors_alt)
		self.assertEqual(s5, s6)
		
		s7 = State(Fields.equi)
		s8 = State(Fields.equi_alt)
		self.assertEqual(s7, s8)
		
		a_set = set()
		s9 = State(Fields.only_18_equi1)
		s10 = State(Fields.only_18_equi2)
		a_set.add(s9)
		self.assertTrue(s10 in a_set)
		

class QueueTest(unittest.TestCase):
	def test_queue(self):
		q = Queue()
		self.assertEqual(len(q), 0)
		q.push(0)
		self.assertEqual(len(q), 1)
		q.push(1)
		self.assertEqual(len(q), 2)
		q.push(2)
		self.assertEqual(len(q), 3)
		self.assertEqual(q.pop(), 0)
		self.assertEqual(len(q), 2)
		self.assertEqual(q.pop(), 1)
		self.assertEqual(len(q), 1)
		self.assertEqual(q.pop(), 2)
		self.assertEqual(len(q), 0)
		self.assertEqual(q.pop(), None)
		self.assertEqual(len(q), 0)
		q.push(0)
		self.assertEqual(len(q), 1)
		self.assertEqual(q.pop(), 0)
		self.assertEqual(len(q), 0)
		
		
		
		
if __name__ == '__main__':
	unittest.main()