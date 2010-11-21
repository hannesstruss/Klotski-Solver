# -*- encoding: utf-8 -*-

class Queue(object):
	def __init__(self):
		self.first_guard = QueueGuard("First")
		self.last_guard = QueueGuard("Last")
		
		self.first_guard.next = self.last_guard
		self.last_guard.prev = self.first_guard
		
		self.count = 0
		
	def push(self, item):
		i = QueueItem(item)
		
		i.prev = self.first_guard
		self.first_guard.next.prev = i
		self.first_guard.next = i
		
		self.count += 1	
	
	def pop(self):
		if self.last_guard.prev is not self.first_guard:
			last_item = self.last_guard.prev
			self.last_guard.prev = last_item.prev
			
			if self.last_guard.prev is self.first_guard:
				self.first_guard.next = self.last_guard
			
			self.count -= 1
			return last_item.data
		return None
	
	def __len__(self):
		return self.count

class QueueGuard(object):
	def __init__(self, name=""):
		self.name = name
		self.prev = self
		self.next = self
		
	def __str__(self):
		return "<Guard %s>" % self.name

class QueueItem(object):
	def __init__(self, data):
		self.data = data
		self.prev = None
		
	def __str__(self):
		return "<Item %s>" % self.data
		
if __name__ == '__main__':
	q = Queue()
	q.push(0)
	q.push(1)
	q.push(2)
	x = q.pop()
	x = q.pop()
	x = q.pop()
	x = q.pop()