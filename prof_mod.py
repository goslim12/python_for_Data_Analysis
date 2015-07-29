from numpy.random import randn

def add_and_sum(x,y):
	added = x+y
	summe = added.sum(axis=1)
	return summe

def call_function():
	x = randn(1000, 1000)
	y = randn(1000, 1000)
	return add_and_sum(x,y)
