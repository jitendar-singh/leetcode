from queue import Queue
import queue
class Solution:
    def filterPods(self, data: str):
        nodes, allpods =[],[]
        for k,v in data.items():
            nodes.append(k)
            allpods.append(v)
        
        for pod in allpods:
            for node in nodes:
                if pod in data[node]:

        

            
            











#         parent, visited, output,queue = {},{},[],Queue()
#         for nodes in data.keys():
#             parent[nodes] = None
#             visited[nodes] = False
        
#         source = "node-1"
#         visited[source] = True
#         queue.put(source)

#         for pods in data.keys():
#             if not visited[pods]:
#                 visited[pods] = True
#                 parent[pods] = 
        

# # Remote worker node
# Cant use a pod twice to form a pair
#Reduction Tech

s= Solution()
adj_list = {"node-1":["pod1","pod23","pod24"],"node-2":["pod11","pod23","pod2"],"node-3":["pod9","pod23","pod2"]}
s.filterPods(adj_list)