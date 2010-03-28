# -*- encoding: utf-8 -*-

class Queue(object):
	def __init__(self, initObj):
		self.first_guard = QueueGuard()
		self.last_guard = QueueGuard()
		
		self.first_guard.next = self.last_guard
		self.last_guard.prev = self.first_guard
		
		self.count = 0
		
		self.push(initObj)
		
	def push(self, item):
		i = QueueItem(item)
		
		i.prev = self.first_guard
		self.first_guard.next.prev = i
		
		self.count += 1	
	
	def pop(self):
		if self.last_guard.prev is not self.first_guard:
			last_item = self.last_guard.prev
			self.last_guard.prev = last_item.prev
			
			self.count -= 1
			
			return last_item.data
		return None
	
	def __len__(self):
		return self.count

class QueueGuard(object):
	def __init__(self):
		self.prev = self
		self.next = self

class QueueItem(object):
	def __init__(self, data):
		self.data = data
		self.prev = None
		
if __name__ == '__main__':
	q = Queue(0)
	q.pop()
	q.pop()