def ft_filter(function, iterable):
    """
    Custom implementation of the built-in filter function.
    Returns a generator of elements for which the function returns True.

    Args:
        function (callable | None): Function applied to each element.
            If None, the bool function is used.
        iterable (iterable): Any iterable to be filtered.

    Returns:
        generator: A generator of elements that satisfy the function.
    """

    if (function is None):
        function = bool

    return (elem for elem in iterable if function(elem))
