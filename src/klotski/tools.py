# -*- encoding: utf-8 -*-

def curry(func, *args, **dict):
	def f(*fargs, **fdict):
		allargs = args + fargs
		dict.update(fdict)
		return func(*allargs, **dict)
		
	return f

if __name__ == '__main__':
	def add(x, y):
		return x+y
	
	add2 = curry(add, 2)
	print add2(3)