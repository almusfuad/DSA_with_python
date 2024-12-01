def post_order(self, current_node):
	if current_node:
		self.post_order(current_node.left_child)
		self.post_order(current_node.right_child)
		print(current_node.data)