adj_list = {
    "A":["B"],
    "B":["A","D","E"],
    "C":["F"],
    "D":["B"],
    "E":["B"],
    "F":["C"]
}

parent, color, trav_time, output = {}, {}, {}, []
time = 0

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1]

def dfs_util(u: str):
    global time

    color[u] = "G"
    trav_time[u][0] = time
    time+=1
    output.append(u)

    for v in adj_list[u]:
        if color[v] == "W":
            color[v] = "G"
            trav_time[u][0] = time
            time+=1
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time+=1

for u in adj_list.keys():
    if color[u] == "W":
        dfs_util(u)
print(output)
for u in trav_time.keys():
    print(u,"-->",trav_time[u])