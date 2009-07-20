# -*- encoding: utf-8 -*-

import unittest

import klotski

equi_1 = (
	(2, 1, 1, 3),
	(2, 1, 1, 3),
	(0, 0, 0, 0),
	(0, 0, 0, 0),
	(0, 0, 0, 0)
)

equi_2 = (
	(3, 1, 1, 2),
	(3, 1, 1, 2),
	(0, 0, 0, 0),
	(0, 0, 0, 0),
	(0, 0, 0, 0)
)

other = (
	(3, 1, 1, 2),
	(3, 1, 1, 2),
	(0, 0, 0, 0),
	(4, 0, 0, 0),
	(4, 0, 0, 0)
)
	

class TestHashCode(unittest.TestCase):
	def testhash(self):
		s1 = klotski.State(equi_1)
		s2 = klotski.State(equi_2)
		otherstate = klotski.State(other)
		self.assertEqual(s1.__hash__(), s2.__hash__())
		self.assertNotEqual(s1.__hash__(), otherstate.__hash__())
		self.assertNotEqual(s2.__hash__(), otherstate.__hash__())