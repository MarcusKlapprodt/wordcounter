import queue
with open("textfile.txt", "r") as textfile:
    data = textfile.read()

# count the total number of words
word_count = 0
for word in data.split(" "):
    word_count += 1

print(word_count)
word_count_text = "The total number of words is: " + str(word_count)


# create a dictionary and put in single words
d = {}
for word in data.split(" "):
    if word in d:
        d[word]=d[word] +1
    else:
        d[word]=1

DictLen = "The size of the used vocabulary is: " + str(len(d))


# creating a Priority Queue and adding the dictionary to the queue
pq = queue.PriorityQueue()

for word, number in d.items():
    pq.put((-number, word))

#printing the result of the 5 most common words
#for i in range(0,5):
#    print(pq.get())


## create pdf
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 21)
        self.cell(80)
        self.cell(30,10, "Wordcounter", 0, 1, "C")
        self.ln(20)
    def body(self):
        self.add_page()
        # Outputs the total Number of words
        self.set_font("Arial", "B", 14)
        self.cell(30,10, "Number of words: ", 0, 1, "L")
        self.set_font("Arial", "", 14)
        self.cell(30, 10, word_count_text, 0, 1, "L")
        self.ln(10)
        # Outputs the size of the dictionary
        self.set_font("Arial", "B", 14)
        self.cell(30, 10, "Vocabulary Size: ", 0, 1, "L")
        self.set_font("Arial", "", 14)
        self.cell(30, 10, DictLen, 0, 1, "L")
        self.ln(10)
        # Outputs the top 20 used words
        self.set_font("Arial", "B", 14)
        self.cell(30, 10, "Top 10 words: ", 0, 1, "L")
        self.set_font("Arial", "", 14)
        for i in range(0, 10):
            self.cell(30, 10, "Word:     '" + str(pq.get()[1]) + "'     "+str(int(-1* pq.get()[0])) + " times", 0, 1, "L")


pdf = PDF("P", "mm", "A4")
pdf.body()



## show the top 20 words used and their count

## output the pdf
pdf.output("simple_demo.pdf")
