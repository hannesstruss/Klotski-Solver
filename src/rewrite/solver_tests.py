# -*- coding: utf-8 -*-
'''
Created on Nov 21, 2010

@author: hannes
'''

import unittest

from klotski_solver import State

class TestHashCodes(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_hash(self):
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
		
		self.assertEqual(hash(state1), hash(state2))
		self.assertNotEqual(hash(state1), hash(state3))
		self.assertNotEqual(hash(state2), hash(state3))
		
		

if __name__ == '__main__':
	unittest.main()