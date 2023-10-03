input_str = input("enter your text: ")


def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_recursion(input_str))
