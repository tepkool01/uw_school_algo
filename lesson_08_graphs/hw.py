import heapq


class Dijkstras:
	def __init__(self, graph):
		self.graph = graph

	def get_shortest_distance(self, start, end):
		# Store distances to all locations from the start, initial node (start) is set to 0
		distances = {node: float('inf') for node in self.graph.keys()}
		distances[start] = 0

		heap_stack = [(0, start)]  # distance, start node name (put distance first for heap sorting)

		while heap_stack:
			# Using a heap for priority queue efficiency
			current_distance, location = heapq.heappop(heap_stack)

			# Ignore paths that are longer
			if current_distance > distances[location]:
				continue

			# Traverse neighbors
			for neighbor, miles in self.graph[location].items():
				# Check distance, if it's smaller, use it. The distances are used as the 'visited'
				new_distance = current_distance + miles
				if new_distance < distances[neighbor]:
					heapq.heappush(heap_stack, (new_distance, neighbor))
					distances[neighbor] = new_distance

		return distances[end]
