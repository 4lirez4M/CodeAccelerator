file = open("file.txt", "r")
content = file.read()
coList = content.split()
letters = 0
for i in content:
    if i.isalpha():
        letters += 1
    continue
space = content.count(" ")

if __name__ == "__main__":
    print(f"The number of letters in the text is: {letters}")
    print(f"The number of words in the text is: {len(coList)}")
    print(f"The number of spaces in the text is: {space}")

