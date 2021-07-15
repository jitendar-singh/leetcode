from queue import Queue

adj_list = {
    "A": ["B","D"],
    "B": ["A","C"],
    "C": ["B"],
    "D": ["A","E","F"],
    "E": ["D","F","G"],
    "F": ["D","E","H"],
    "G": ["E","H"],
    "H": ["G","F"]
}

visited, level, parent, output, queue = {}, {}, {}, [], Queue()

for node in adj_list.keys():
    parent[node] = None
    visited[node] = False
    level[node] = -1

root = "A"
visited[root] = True
level[root] = 0
queue.put(root)

while not queue.empty():
    u = queue.get()
    visited[u] = True
    output.append(u)

    for vertices in adj_list[u]:
        if not visited[vertices]:
            visited[vertices] = True
            parent[vertices] = u
            level[vertices] = level[u]+1
            queue.put(vertices)
print(output)

destination = "G"
path = []
while destination is not None:
    path.append(destination)
    destination = parent[destination]
path.reverse()
print(path)



