# -*- encoding: utf-8 -*-

class Queue(object):
	def __init__(self, initObj):
		i = QueueItem(initObj)
		self.__first = i
		self.__last = i
		i.prev = i
		self.count = 1
		
	def push(self, item):
		i = QueueItem(item)
		self.__first.prev = i
		self.__first = i
		self.count += 1	
		
	
	def pop(self):
		i = self.__last
		self.__last = self.__last.prev 
		self.count -= 1
		return i.data
	
	def __len__(self):
		return self.count

class QueueItem(object):
	def __init__(self, data):
		self.data = data
		self.prev = None