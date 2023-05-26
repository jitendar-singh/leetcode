from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited vertices
    queue = deque([start])  # Initialize the queue with the starting vertex
    
    while queue:
        vertex = queue.popleft()  # Retrieve the first vertex from the queue
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Process the vertex (here, we print it)
            # Enqueue the adjacent vertices of the current vertex
            queue.extend(adjacent for adjacent in graph[vertex] if adjacent not in visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # Output: A B C D E F
