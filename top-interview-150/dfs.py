def dfs(graph, start):
    visited = set()  # Set to track visited vertices
    stack = [start]  # Stack to keep track of vertices to visit
    
    while stack:
        vertex = stack.pop()  # Pop the top vertex from the stack
        
        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited
            print(vertex)  # Process the vertex (e.g., print it)
            
            # Add the unvisited neighboring vertices to the stack
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Example usage
adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(adjacency_list, 'A')
