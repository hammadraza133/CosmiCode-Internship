from collections import Counter, defaultdict, namedtuple

# Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
word_count = Counter(words)
print(word_count)

# defaultdict
grades = [('John', 85), ('Alice', 90), ('John', 78)]
student_scores = defaultdict(list)
for name, score in grades:
    student_scores[name].append(score)
print(student_scores)

# namedtuple
Person = namedtuple("Person", "name age")
p1 = Person(name="John", age=30)
print(p1.name, p1.age)
