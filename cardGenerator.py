import re

front = open("FrontSubtitles.txt").read()
back = open("BackSubtitles.txt").read()

frontMatches = re.findall(r'(\d+ --> \d+)\n(.+?)(?=\d+ --> \d+)', front, flags=re.MULTILINE|re.DOTALL)
backMatches = re.findall(r'(\d+ --> \d+)\n(.+?)(?=\d+ --> \d+)', back, flags=re.MULTILINE|re.DOTALL)

for match in frontMatches:
    print(match)
for match in backMatches:
    print(match)