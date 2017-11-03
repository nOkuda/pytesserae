"""Example for using pytesserae.score"""
import pytesserae.score as score


def _run():
    """Example of how to score a match"""
    matching_terms = {'a', 'b'}
    source_counts = {'a': 10, 'b': 50, 'c': 25}
    target_counts = {'a': 4, 'b': 73, 'c': 15}
    source_chunk = ['a', 'b']
    target_chunk = ['a', 'c', 'b']
    source_distance = score.find_distance(
        matching_terms, source_chunk, source_counts)
    target_distance = score.find_distance(
        matching_terms, target_chunk, target_counts)
    match_score = score.vanilla(
        matching_terms, source_distance, target_distance, source_counts,
        target_counts)
    print('Calculated score:', match_score)


if __name__ == '__main__':
    _run()
