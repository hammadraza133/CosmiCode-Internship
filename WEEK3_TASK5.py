f = open("text.txt", "r")
text = f.read().lower().replace(".", "").replace(",", "")
f.close()
words = text.split()
counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1
max_word = max(counts, key=counts.get)
print("Most frequent word:", max_word)
