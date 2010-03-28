from operator import attrgetter

import unittest

from klotski import State

class Fields(object):
	trivial = (
		(0, 1, 1, 0),
		(0, 1, 1, 0),
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

class TestState(unittest.TestCase):
	def test_init(self):
		s = State(Fields.trivial)
		self.assertEqual(len(s.blocks), 1)
		self.assertEqual(s.field, Fields.trivial)
		
		s = State(Fields.blocked1)
		self.assertEqual(len(s.blocks), 3)
		
		s = State(Fields.blocked2)
		self.assertEqual(len(s.blocks), 1)
		
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
		
		
if __name__ == '__main__':
	unittest.main()