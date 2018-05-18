
"""Converts the output of the search function into LaTeX code"""
import re


def latex(matchList):
    output = []
    for l in matchList:
        # locate match in asterisks
        match = re.search(r'\*[a-zA-Z]+\*', l)
        markedMatch = match.group()
        # highlight remaining match
        highlight = l.replace(markedMatch, r'\textcolor{red}{'+markedMatch+r'}}'.format(markedMatch))
        # remove asterisks
        highlight = highlight.replace("*", "")
        output.append(highlight)

    return output
