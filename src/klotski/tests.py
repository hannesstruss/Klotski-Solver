from calendar import main
import unittest

from klotski import State

class TestState(unittest.TestCase):
	def test_init(self):
		s = State((
			(0, 1, 1, 0),
			(0, 1, 1, 0),
			(0, 0, 0, 0),
			(0, 0, 0, 0),
			(0, 0, 0, 0)
		))
		
		self.assertEqual(len(s.blocks), 1)
		
if __name__ == '__main__':
	unittest.main()