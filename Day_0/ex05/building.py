import sys


def building(text: str):
    """
    Counts each occurence of differents type of character
    in the given string

    Args:
        text (str): string to occur on
    Raises:
        TypeError: if the argument is not a string
    Returns:
        None: prints the occurences of each type of character
    """

    if text is None:
        text = input("What is the text to count?\n")
    if not isinstance(text, str):
        raise TypeError("TypeError: text must be a string")

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
    """
    Validates input arguments and calls the building function.
    Args:
        sys.argv[1]: string to count characters in
    Raises:
        AssertionError: if the arguments are bad (more than one argument)
    Returns:
        int: exit code (0 for success, 1 for error)
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: more than one argument is\
                                provided")
        elif len(sys.argv) == 1:
            building(None)
        else:
            building(sys.argv[1])
    except AssertionError as err:
        print(err)
        return 1
    except Exception as err:
        print(err)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
