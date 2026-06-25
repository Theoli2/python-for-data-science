import sys
from ft_filter import ft_filter


def main():
    """
    Validates input arguments and prints words longer than a given length.

    Args:
        sys.argv[1]: string to filter
        sys.argv[2]: number of character in a word for it to not be filtered
    Raises:
        AssertionError: if the arguments are bad (not enough, too many, or\
        invalid)
    Returns:
        None: prints the filtered list of words
    """

    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        string = sys.argv[1]
        if not isinstance(string, str) or not string.strip():
            raise AssertionError("AssertionError: the arguments are bad")
        try:
            N = int(sys.argv[2])
        except (TypeError, ValueError):
            raise AssertionError("AssertionError: the arguments are bad")
        result = list(ft_filter(lambda word: len(word) > N, string.split()))
        print(result)
    except Exception as err:
        print(err)
        return 1
    return 0


if __name__ == "__main__":
    main()
