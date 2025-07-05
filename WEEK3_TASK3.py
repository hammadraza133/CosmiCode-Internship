sentence = input("Enter a sentence: ")
words = sentence.replace(".", "").replace(",", "").split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
