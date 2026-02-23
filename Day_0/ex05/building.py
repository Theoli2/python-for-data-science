import sys


def building(text: any):
    """
    Counts each occurence of differents type of character
    in the given string

    Args:
        text (str): string to occur on
    """

    if text is None:
        text = input("What is the text to count?\n")

    upper = lower = punctuation = spaces = digits = 0
    for char in text:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char.isspace():
            spaces += 1
        if char.isdigit():
            digits += 1
        else:
            punctuation += 1

    total = upper + lower + digits + spaces + punctuation
    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    elif len(sys.argv) == 1:
        building(None)
    else:
        building(sys.argv[1])
    return 0


if __name__ == "__main__":
    main()
