adj_list = {
    "A": ["B", "C"],
    "B": ["A","D"],
    "C":["A", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}
for key,value in adj_list.items():
    print(key,':',value)

print(adj_list["B"])

adj_list["A"].append("D")
adj_list["D"].append("A")

for key,value in adj_list.items():
    print(key,':',value)

print(f'Degree of A - > {len(adj_list["A"])}')