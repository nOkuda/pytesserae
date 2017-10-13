import re
with open('theDunwichHorror.txt', 'r') as f:
    foundLines = []
    for line in f:
        result = re.search('ridiculous', line)
        if result:
            highlight = line.replace('ridiculous', '*{}*'.format('ridiculous'))
            foundLines.append(highlight)
    for l in foundLines:
        print(l)
