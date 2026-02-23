import sys
from ft_filter import ft_filter


def main():
    '''
    Validates input arguments and prints words longer than a given length.

    Args:
        sys.argv[1]: string to filter
        sys.argv[2]: number of character in a word for it to not be filtered
    '''

    if len(sys.argv) < 3:
        raise AssertionError("the arguments are bad")
    string = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    if not string.strip():
        raise AssertionError("the arguments are bad")
    result = list(ft_filter(lambda word: len(word) > N, string.split()))
    print(result)


if __name__ == "__main__":
    main()
