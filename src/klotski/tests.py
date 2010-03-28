from calendar import main
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

class TestState(unittest.TestCase):
	def test_init(self):
		s = State(Fields.trivial)
		
		self.assertEqual(len(s.blocks), 1)
		self.assertEqual(s.field, Fields.trivial)
		
		
if __name__ == '__main__':
	unittest.main()