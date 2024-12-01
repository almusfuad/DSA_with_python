
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None


def push(self, data):
	new_node = Node(data)
	if self.top:
		new_node.next = self.top
	self.top = new_node