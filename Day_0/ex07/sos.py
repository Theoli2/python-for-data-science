import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-.. ",
    "e": ". ",
    "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.-- ",
    "z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- "
}


def is_valid_string(text, dictionary):
    """
    Return True if all characters of text are keys in morse_dict."
    Args:
        text (str): string to check
        dictionary (dict): dictionary to check against
    Returns:
        bool: True if all characters are in the dictionary, False otherwise
    """
    return all(char in dictionary for char in text)


def convert_to_morse(text, dictionary):
    """
    Returns the conversion of the text passed in parameter as the values in\
        the dictionary
    Args:
        text (str): string to convert
        dictionary (dict): dictionary to use for conversion
    Raises:
        ValueError: if the text contains characters not in the dictionary
    Returns:
        str: the converted string
    """
    if not is_valid_string(text, dictionary):
        raise ValueError("The arguments are bad")
    return "".join(dictionary.get(char, char) for char in text)


def main():
    """
    Convert the command-line argument to Morse and print it.
    Args:
        sys.argv[1]: string to convert to Morse code
    Raises:
        AssertionError: if the arguments are bad (not exactly one argument)
    Returns:
        None: prints the converted Morse code
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        output = convert_to_morse(string, NESTED_MORSE)
        print(output)
    except Exception as err:
        print(err)
        return 1


if __name__ == "__main__":
    main()
