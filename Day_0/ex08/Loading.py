from os import get_terminal_size


def ft_tqdm(lst: range):
    """
    Creates a tqdm-like progress bar for iterating through a range/list.
    Adapts the progress bar width to the terminal size.
    """
    total = len(lst)
    terminal_width = get_terminal_size().columns
    reserved = 34 + len(str(total)) * 2
    bar_width = max(terminal_width - reserved, 10)

    for i, elem in enumerate(lst):
        percent = (i + 1) / total * 100
        filled = int(bar_width * (i + 1) // total)
        bar = '█' * filled + ' ' * (bar_width - filled)
        print(f'\r{percent:.0f}%|{bar}| {i + 1}/{total}', end='', flush=True)
        yield elem
    print()
