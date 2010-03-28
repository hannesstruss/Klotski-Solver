from calendar import main
import unittest

from klotski import State

class TestState(unittest.TestCase):
	def test_init(self):
		trivial = (
			(0, 1, 1, 0),
			(0, 1, 1, 0),
			(0, 0, 0, 0),
			(0, 0, 0, 0),
			(0, 0, 0, 0)
		)
		
		s = State(trivial)
		
		self.assertEqual(len(s.blocks), 1)
		self.assertEqual(s.field, trivial)
		
		
		
		
		
if __name__ == '__main__':
	unittest.main()