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

parent, level, visited, output, queue = {}, {}, {}, [], Queue()


for node in adj_list.keys():
    parent[node] = None
    visited[node] = False
    level[node] = -1

source = "A"
visited[source] = True
level[source] = 0
queue.put(source)

while(not queue.empty()):
    u = queue.get()
    output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            parent[v] = u
            level[v] = level[u]+1
            visited[v] = True
            queue.put(v)
print(output)

print(level)

v = "G"
path = []

while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)