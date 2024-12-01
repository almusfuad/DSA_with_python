def dfs(visited_vertices, graph, current_vertex):
	if current_vertix not in visited_vertics:
		print(current_vertex)
		visited_vertices.add(current_vertex)
		for adjacent_vertex in graph[current_vertex]:
			dfs(visited_vertices, graph, adjacent_vertex)