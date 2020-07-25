import re

front = open("FrontSubtitles.txt").read()
back = open("BackSubtitles.txt").read()

def createMatchObject(string):
    matches = re.findall(r'(\d+ --> \d+)\n(.+?)(?=\d+ --> \d+)', string, flags=re.MULTILINE|re.DOTALL)
    return { time : line for time,line in matches }


frontMatches = createMatchObject(front)
backMatches = createMatchObject(back)

for key, value in frontMatches.items():
    print(key, '->', value)

for key, value in backMatches.items():
    print(key, '->', value)
