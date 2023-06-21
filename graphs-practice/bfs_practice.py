from queue import Queue

adj_list = {
    "A": ["B", "C"],
    "B": ["A","D"],
    "C":["A", "D", "E"],
    "D": ["A", "C"],
    "E": ["C"]
}

visited, level, parent, ouput  = {}, {}, {}, []

for nodes in adj_list.keys():
    visited[nodes] = False
    level[nodes] = -1
    parent[nodes] = None

queue = Queue()
source = "A"
visited[source] = True
level[source] = 0

queue.put(source)

while not queue.empty():
    u = queue.get()

    ouput.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            level[v] = level[u]+1
            parent[v] = u
            queue.put(v)

print(ouput)
print(parent)