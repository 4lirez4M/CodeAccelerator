from collections import Counter

file = open("file.txt", "r")
content = file.read()
coList = content.split()
counts = Counter(coList)
for item in counts:
    if counts[item] > 1:
        print(f"item: {item}, count: {counts[item]}")

