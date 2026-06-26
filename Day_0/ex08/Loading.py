from os import get_terminal_size


def ft_tqdm(lst: range):
    """
    Creates a tqdm-like progress bar for iterating through a range/list.
    Adapts the progress bar width to the terminal size.
    Makes sure the progress bar does not exceed the terminal width\
 to avoid line wrapping.

    Args:
        lst (range): A range or list to iterate through
    Raises:
        AssertionError: If the input is not a range or list
    Returns:
        generator: A generator that yields elements from the input range/list
    """

    if not isinstance(lst, (range, list)):
        raise AssertionError("Input must be a range or list")
    total = len(lst)
    terminal_width = get_terminal_size().columns
    reserved = 34 + len(str(total)) * 2
    bar_width = max(terminal_width - reserved, 10)

    for i, elem in enumerate(lst):
        percent = (i + 1) / total * 100
        filled = int(bar_width * (i + 1) // total)
        bar = '█' * filled + ' ' * (bar_width - filled)
        output = f'{percent:.0f}%|{bar}| {i + 1}/{total}'
        output = output[:terminal_width]
        print(f'\r{output}', end='', flush=True)
        yield elem
    print()
