adj_list = {
    "A":["B"],
    "B": ["A","D","E"],
    "C": ["F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"]
}

parent, output, color, trav_time = {}, [], {}, {}
for node in adj_list.keys():
    parent[node] = None
    color[node] = "W"
    trav_time[node] = [-1,-1]

time = 0

def dfs_util(u):
    global time

    color[u] = "G"
    trav_time[u][0] = time
    time+=1
    output.append(u)

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time+=1

for v in adj_list.keys():
    if color[v] == "W":
        dfs_util(v)
print(output)


