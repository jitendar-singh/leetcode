from collections import deque

queque = deque(["Jitendar","Monalisa","Sunny","Sony"])
print(queque)
queque.append("Shavi")
print(queque)

queque.popleft()
print(queque)
queque.appendleft("Jitendar")
print(queque)
queque.remove("Sunny")
print(queque)
queque.insert(2,"Fusi")
print(queque)
queque.reverse()
print(list(queque))
