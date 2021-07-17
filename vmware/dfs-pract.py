adj_list = {
    "A":["B"],
    "B":["A","D","E"],
    "C":["F"],
    "D":["B"],
    "E":["B"],
    "F":["C"]
}

color, parent, output, trav_time = {}, {}, [], {}
time = 0

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

def dfs_util(u: str) -> None:
    global time
    color[u] = "G"
    trav_time[u][0] = time
    output.append(u)

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time+=1

for node in adj_list.keys():
    if color[node] == "W":
        dfs_util(node)
print(output)

for node in adj_list.keys():
    print(node,"--->",trav_time[node])