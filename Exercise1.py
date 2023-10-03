def count_character(string):
    special_character = 0
    characters = 0
    numbers = 0

    for i in range(0, len(string)):

        if string[i].isdigit():
            numbers += 1
        elif string[i].isalpha():
            characters += 1
        else:
            special_character += 1

    print(f"special char:{special_character} char:{characters} num:{numbers}")


if __name__ == "__main__":
    paragraph = input("Enter your paragraph:")
    count_character(paragraph)




