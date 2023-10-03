file = open("file.txt", "r")
words = 0
counter = 0
content = file.read()
coList = content.split("\n")
for item in coList:
    if 4 < len(item.split(" ")):
        counter += 1
for item in coList:
    words += len(item.split())
print(words)
print(counter)


