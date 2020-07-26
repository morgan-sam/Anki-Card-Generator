import re
import genanki

front = open("FrontSubtitles.txt").read()
back = open("BackSubtitles.txt").read()


def removeNewLineChars(string):
    string = re.sub(r'\n', ' ', string)
    if (string.endswith(' ')):
        string = string[:-1]
    return string


def createMatchObject(string):
    matches = re.findall(r'(\d+ --> \d+)\n(.+?)(?=\d+ --> \d+)',
                         string, flags=re.MULTILINE | re.DOTALL)
    return {time: removeNewLineChars(line) for time, line in matches}


def printObject(obj):
    for key, value in obj.items():
        print(key, '->', value)


def generateCardArray(frontMatches, backMatches):
    return [{"front": value, "back": backMatches[key]} for key, value in frontMatches.items() if key in backMatches]


frontMatches = createMatchObject(front)
backMatches = createMatchObject(back)
cardArray = generateCardArray(frontMatches, backMatches)

anki_model = genanki.Model(
    1607392319,
    'Card Model',
    fields=[
        {'name': 'Target'},
        {'name': 'Source'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Target}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Source}}',
        },
    ])

anki_deck = genanki.Deck(
    2059400110,
    'Language Subtitles')

for val in cardArray:
    anki_note = genanki.Note(
        model=anki_model,
        fields=[val["front"], val["back"]])
    anki_deck.add_note(anki_note)

genanki.Package(anki_deck).write_to_file('language_subtitles.apkg')
