import queue
with open("textfile.txt", "r") as textfile:
    data = textfile.read()

# create a dictionary and put in single words
d = {}
for word in data.split(" "):
    if word in d:
        d[word]=d[word] +1
    else:
        d[word]=1

# creating a Priority Queue and adding the dictionary to the queue
pq = queue.PriorityQueue()

for word, number in d.items():
    pq.put((-number, word))

#printing the result of the 5 most common words
for i in range(0,5):
    print(pq.get())

## Export the outpunt in a pdf file


## show the total number of words

## show the total number of characters

## show the top 20 words used and their count


