def bfs(self):
	if self.root:
		visited_nodes = []
		bfs_queue = queue.SimpleQueue()
		bfs_queue.put(self.root)
		while not bfs_queue.empty():
			current_node = bfs_queue.get()
			visited_nodes.append(current_node.data)
			if current_node.left:
				bfs_queue.put(current_node.left)
			if current_node.right:
				bfs_queue.put(current_node.right)
		return visited_nodes