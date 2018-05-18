"""A function for finding matching tokens in two lists"""


def match(source, target):
    """Returns matching tokens from two lists of words

    Parameters
    ----------
    source : [str]
        A list of tokens from the source text
    target : [str]
        A list of tokens from the target text, to be compared
        with the source

    Returns
    -------
    [str]
        A list of tokens common to both input lists
    """
    return list(set(source).intersection(set((target))))
