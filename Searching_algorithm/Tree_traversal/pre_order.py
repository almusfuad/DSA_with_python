def pre_order(self, current_node):
	if current_node:
		print(current_node.data)
		self.pre_order(current_node.left_child)
		self.pre_order(current_node.right_child)