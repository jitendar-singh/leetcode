adj_list = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B","F"],
    "D":[],
    "E":["F"],
    "F":[]
}

color, parent, output,trav_time = {}, {}, [], {}

for nodes in adj_list.keys():
    parent[nodes] = None
    color[nodes] = 'W'
    trav_time[nodes] = [-1,-1]

# print(parent)
# print(trav_time)
# print(color)
time = 0
def dfs_util(u):
    global time
    color[u] = 'G'
    trav_time[u][0] = time
    output.append(u)
    time+=1

    for v in adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time+=1

dfs_util("A")
print(output)
print(parent)
print(trav_time)