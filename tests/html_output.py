"""Converts the output of the search function to html code"""
def html(matchList):
    output = []
    for l in matchList:
        match = re.compile(r'\*[a-zA-Z]\*')
        literal = match.group()
        highlight = re.sub(literal, '<span style="color: red">{}</span>'.format(literal), l)
