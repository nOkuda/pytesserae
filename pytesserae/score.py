"""Module for Tesserae scoring"""
import math


def vanilla(
    matching_terms,
    source_distance, target_distance,
    source_counts, target_counts
):
    """Calculates the Tesserae score between from_source and from_target

        * matching_terms :: {str}
            A set of words found to match between the source and target
        * source_distance, target_distance :: int
            Distance between least frequent matching terms for source and
            target, respectively
        * source_counts, target_counts :: {str: int}
            A dictionary of word counts to consult in looking up frequency
            information

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
    """
    return math.log(
        (
            sum([1 / target_counts[t] for t in matching_terms]) +
            sum([1 / source_counts[s] for s in matching_terms])
        ) / (target_distance + source_distance)
    )
