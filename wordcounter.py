import queue
with open("textfile.txt", "r") as textfile:
    data = textfile.read()

d = {}
for word in data.split(" "):
    if word in d:
        d[word]=d[word] +1
    else:
        d[word]=1
print(d)

pq = queue.PriorityQueue()

for word, number in d.items():
    pq.put((-number, word))
for i in range(0,5):
    print(pq.get())

