# -*- encoding: utf-8 -*-

class Stack(object):
	def __init__(self):
		self.__top = None
		self.count = 0
		
	def push(self, item):
		i = StackItem(item)
		i.next = self.__top
		self.__top = i
		self.count += 1
		
	def pop(self):
		i = self.__top
		self.__top = i.next
		self.count -= 1
		return i.data
	
	def peak(self):
		return self.__top.data
	
	def __len__(self):
		return self.count
	
class StackItem(object):
	def __init__(self, data):
		self.data = data
		self.next = None