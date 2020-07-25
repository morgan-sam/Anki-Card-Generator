import re

front = open("FrontSubtitles.txt").read()
back = open("BackSubtitles.txt").read()

def removeNewLineChars(string):
    string = re.sub(r'\n', ' ', string)
    if (string.endswith(' ')): string = string[:-1]
    return string


def createMatchObject(string):
    matches = re.findall(r'(\d+ --> \d+)\n(.+?)(?=\d+ --> \d+)', string, flags=re.MULTILINE|re.DOTALL)
    return { time : removeNewLineChars(line) for time, line in matches }

def printObject(obj):
    for key, value in obj.items():
        print(key, '->', value)

frontMatches = createMatchObject(front)
backMatches = createMatchObject(back)

cardArray = []

for key, value in frontMatches.items():
    if key in backMatches:
        cardArray.append({"front": value, "back": backMatches[key] })

for val in cardArray:
    print(val)