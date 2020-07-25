import re

front = open("FrontSubtitles.txt").read()
back = open("BackSubtitles.txt").read()

def createMatchObject(string):
    matches = re.findall(r'(\d+ --> \d+)\n(.+?)(?=\d+ --> \d+)', string, flags=re.MULTILINE|re.DOTALL)
    return { time : line for time,line in matches }

def printObject(obj):
    for key, value in obj.items():
        print(key, '->', value)

frontMatches = createMatchObject(front)
backMatches = createMatchObject(back)

printObject(frontMatches)
printObject(backMatches)