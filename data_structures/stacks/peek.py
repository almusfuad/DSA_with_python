class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None


def peek(self):
	if self.top:
		return self.top.data
	else:
		return None