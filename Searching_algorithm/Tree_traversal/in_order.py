def in_order(self, current_node):
	if current_node:
		self.in_order(current_node.left_child)
		print(current_node.data)
		self.in_order(current_node.right_child)