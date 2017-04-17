import queue

q = queue.Queue()

for i in range(10):
    q.put(i)

print(q.empty())
print(q.qsize())