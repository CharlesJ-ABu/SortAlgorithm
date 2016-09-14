import random

def randata():
	a = []
	for i in range(1000):
		a.append(random.randint(0, 1000))
	return a
