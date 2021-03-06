def coding_problem_05():
    """
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
    Given this implementation of cons below, implement car and cdr.

    >>> def cons(a, b):
    ...     def pair(f):
    ...         return f(a, b)
    ...     return pair

    >>> car, cdr = coding_problem_05()
    >>> car(cons('first', 'last')) == 'first'
    True

    >>> cdr(cons('first', 'last')) == 'last'
    True
    """
    def car(f):
        return f(lambda a, b: a)

    def cdr(f):
        return f(lambda a, b: b)

    return car, cdr


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
