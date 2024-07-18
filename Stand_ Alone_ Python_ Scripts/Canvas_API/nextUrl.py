import re
def nextUrl(linkTxt):
    url = None
    if linkTxt:
        links = linkTxt.split(",")
        nextRegEx = re.compile('^<(.*)>; rel="next"$')
        for i in range(len(links)):
            matches = nextRegEx.match(links[i])
            if matches:
                url = matches.group(1)
    return url