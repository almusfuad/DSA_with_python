class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left_child = left
		self.right_child = right


class BinarySearchTree:
	def __init__(self):
		self.root = None


def search(self, search_value):
	current_node = self.root

	while current_node:
		if search_value == current_node.data:
			return True
		elif search_value < current_node.data:
			current_node = current_node.left_child
		else:
			current_node = current_node.right_child

	return False


