import sys


def whatis(object: any):
    try:
        num = int(object)
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    if len(sys.argv) < 2:
        sys.exit(1)

    whatis(sys.argv[1])
