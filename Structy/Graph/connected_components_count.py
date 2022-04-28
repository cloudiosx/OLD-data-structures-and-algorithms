# Time: O(e) or O(n^2) | Space: O(n) | e = # of edges, n = # of nodes, n^2 = # of edges

def connected_components_count(graph):
	visited = set()
	count = 0

	for node in graph:
		if explore(graph, node, visited) == True:
			count += 1

	return count

def explore(graph, current, visited):
	if current in visited:
		return False

	visited.add(current)

	for neighbor in graph[current]:
		explore(graph, neighbor, visited)

	return True