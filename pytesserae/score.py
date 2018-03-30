"""Module for Tesserae scoring"""
import math


def vanilla(
    matching_terms,
    source_distance, target_distance,
    source_counts, target_counts,
):
    """Calculates the Tesserae score between source and target units

    Parameters
    ----------
    matching_terms : {str}
        A set of words found to match between the source and target
    source_distance, target_distance : int
        Distance between least frequent matching terms for source and
        target, respectively
    source_counts, target_counts : {str: int}
        A dictionary of word counts to consult in looking up frequency
        information

    Returns
    -------
    float
        The Tesserae score between source and target units

    Notes
    -----
    The scoring function is defined in [1]_.

    Note that frequency for some word x in some text y refers to the number of
    times x appears in y divided by the total number of tokens in y.

    score = ln (
        (
            sum([1/f(t) for t in matching_terms]) +
            sum([1/f(s) for s in matching_terms])
        )
        / (d_t + d_s)
    )
        * f(t) is the frequency of a matching term in the target
        * f(s) is the frequency of a matching term in the source
        * d_t = target_distance
        * d_s = source_distance

    References
    ----------
    .. [1] N. Coffee, C. Forstall, T. Buck, K. Roache, S. Jacobson, "Modeling
       the Scholars: Detecting Intertextuality through Enhanced Word-Level
       N-Gram Matching," Digital Scholarship in the Humanities vol. 30.4, pp.
       503-515, 2014.

    Examples
    --------
    Begin with a unit from the source and from the target.

    >>> source_chunk = ['a', 'b']
    >>> target_chunk = ['a', 'c', 'b']

    Consider the terms that match across both units.

    >>> matching_terms = {'a', 'b'}

    Count statistics for source and target texts.

    >>> source_counts = {'a': 10, 'b': 50, 'c': 25}
    >>> target_counts = {'a': 4, 'b': 73, 'c': 15}

    Calculate distance information.

    >>> source_distance = score.find_distance(
    ...     matching_terms, source_chunk, source_counts)
    >>> target_distance = score.find_distance(
    ...     matching_terms, target_chunk, target_counts)

    Now score the units.

    >>> score.vanilla(
    ...     matching_terms, source_distance, target_distance, source_counts,
    ...     target_counts)
    2.4411948928528475

    """
    target_size = sum([v for v in target_counts.values()])
    source_size = sum([v for v in source_counts.values()])
    return math.log(
        (
            sum([1 / (target_counts[t]/target_size) for t in matching_terms]) +
            sum([1 / (source_counts[s]/source_size) for s in matching_terms])
        ) / (target_distance + source_distance)
    )


def _get_two_lowest(matching_terms, counts):
    """Gets two lowest frequency matching terms

    Assumes that len(matching_terms) >= 2

    Parameters
    ----------
    matching_terms : {str}
        The set of matching words
    counts : {str: int}
        A dictionary of word counts for the text from which the chunk
        comes

    Returns
    -------
    lowest_term : str
        lowest frequency term
    next_lowest_term : str
        second lowest frequency term

    Examples
    --------
    >>> matching_terms = {'a', 'b'}
    >>> counts = {'a': 5, 'b': 10}
    >>> _get_two_lowest(matching_terms, counts)
    'a', 'b'

    >>> matching_terms = {'a', 'b', 'c'}
    >>> counts = {'a': 5, 'b': 10, 'c': 1}
    >>> _get_two_lowest(matching_terms, counts)
    'c', 'a'
    """
    assert len(matching_terms) >= 2, 'not enough matching terms'
    match_tuple = tuple(matching_terms)
    # lowest and next_lowest are tuples of (term, count)
    lowest = (match_tuple[0], counts[match_tuple[0]])
    next_lowest = (match_tuple[1], counts[match_tuple[1]])
    if lowest[1] > next_lowest[1]:
        tmp = lowest
        lowest = next_lowest
        next_lowest = tmp
    for term in match_tuple[2:]:
        term_count = counts[term]
        if term_count < lowest[1]:
            next_lowest = lowest
            lowest = (term, term_count)
        elif term_count < next_lowest[1]:
            next_lowest = (term, term_count)
    return lowest[0], next_lowest[0]


def _get_indices(term, chunk):
    """Get indices where term appears in chunk

    Parameters
    ----------
    term : str
        The token to look for in the `chunk`
    chunk : [str]
        A chunk of text in which to look for instances of `term`

    Returns
    -------
    [int]
        Indices in `chunk` where `term` was found

    Examples
    --------
    >>> term = 'a'
    >>> chunk = ['a', 'a', 'b', 'b', 'a']
    >>> _get_indices(term, chunk)
    [0, 1, 5]

    """
    return [i for i, token in enumerate(chunk) if token == term]


def find_distance(matching_terms, chunk, counts):
    """Calculates distance between matching terms in given chunk

    When there is only one matching term, the distance should be the smallest
    between instances of the matching term in chunk.

    Where there is more than one matching term, the distance should be the
    smallest between the instances of the lowest frequency matching term and
    the instances of the second lowest frequency matching term.

    Parameters
    ----------
    matching_terms : {str}
        The set of matching words
    chunk : [str]
        A chunk of text
    counts : {str: int}
        A dictionary of word counts for the text from which the chunk
        comes

    Returns
    -------
    int
        The distance between the two lowest frequency terms in the chunk

    Examples
    --------
    >>> matching_terms = {'a', 'b'}
    >>> chunk = ['a', 'b', 'c', 'd']
    >>> counts = {'a': 2, 'b': 2, 'c': 50, 'd': 25}
    >>> find_distance(matching_terms, chunk, counts)
    1

    """
    if len(matching_terms) == 1:
        # handle case where same term shows up multiple times in chunk
        term = tuple(matching_terms)[0]
        positions = _get_indices(term, chunk)
        # if this becomes a bottleneck, there is always numpy.diff
        inter_position_diffs = [
            j - i for i, j in zip(positions[:-1], positions[1:])]
        return min(inter_position_diffs)

    term1, term2 = _get_two_lowest(matching_terms, counts)
    term1_positions = _get_indices(term1, chunk)
    term2_positions = _get_indices(term2, chunk)
    # following lines might be improved with better algorithm
    min_dist = abs(term1_positions[0] - term2_positions[0])
    for pos1 in term1_positions:
        for pos2 in term2_positions:
            cur_dist = abs(pos2 - pos1)
            if cur_dist < min_dist:
                min_dist = cur_dist
    return min_dist
