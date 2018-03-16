from collections import Counter

source = ['banana', 'Rui Chaves', 'Rui Chaves']
target = ['Mickey Mouse', 'Rui Chaves', 'banana']

def matchify(source, target):
    # Returns matched tokens from two texts w/ the frequencies of each
    source_dict = Counter(source)
    target_dict = Counter(target)
    # Creates dictionaries of frequencies indexed by tokens
    matches = list(set(source).intersection(target))
    # Creates a list of matches
    print(matches)
    i = 0
    for match in matches:
        # Prints the num of occurences of each item in matches
        print(source_dict[matches[i]])
        print(target_dict[matches[i]])
        i =+ 1

matchify(source, target)
