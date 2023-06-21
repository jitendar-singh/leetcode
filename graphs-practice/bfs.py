from queue import Queue

adj_list = {
    "A": ["B", "C"],
    "B": ["A","D"],
    "C":["A", "D", "E"],
    "D": ["B", "C"],
    "E": ["C", "D"]
}

visited, level, parent, bfs_traversal_output = {}, {}, {}, []
queue = Queue()
for node in adj_list.keys():
    visited[node] = False
    level[node] = -1
    parent[node] = None

# print(visited)
# print(parent)
# print(level)

source = "A"
visited[source] = True
level[source] = 0
queue.put(source)

while not queue.empty():
     u = queue.get()
    #  print(u)
     bfs_traversal_output.append(u)
     for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)
print(bfs_traversal_output)
print(level)
print(parent)