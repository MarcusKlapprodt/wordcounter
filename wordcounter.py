import queue
with open("textfile.txt", "r") as textfile:
    data = textfile.read()

# count the total number of words
word_count = 0
for word in data.split(" "):
    word_count += 1

print(word_count)
word_count_text = "The total number of words is " + str(word_count)


# create a dictionary and put in single words
d = {}
for word in data.split(" "):
    if word in d:
        d[word]=d[word] +1
    else:
        d[word]=1

DictLen = "The total number of different words is " + str(len(d))


# creating a Priority Queue and adding the dictionary to the queue
pq = queue.PriorityQueue()

for word, number in d.items():
    pq.put((-number, word))

#printing the result of the 5 most common words
for i in range(0,5):
    print(pq.get())

## Export the outpunt in a pdf file


## create pdf
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)

## show the total number of words
pdf.cell(200, 100, txt=word_count_text, ln=1, align="C")

## show the number of individual words
pdf.cell(200, 200, txt=DictLen, ln=1, align="C")

## show the top 20 words used and their count

## output the pdf
pdf.output("simple_demo.pdf")
