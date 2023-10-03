text = input("Enter your text: ")


def reverse(text):
    string = ""
    for i in text:
        string = i + string
    return string


print("The original string is: ", end="")
print(text)

print("The reversed string is: ", end="")
print(reverse(text))












