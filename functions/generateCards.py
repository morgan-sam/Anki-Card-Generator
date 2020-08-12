import re
import genanki
from functions.convertTextToMp3 import convertTextToMp3


def generateDeck(cardArray):

    anki_model = genanki.Model(
        1607392319,
        'Card Model',
        fields=[
            {'name': 'Target'},
            {'name': 'Source'},
            {'name': 'Audio'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Target}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Source}}<br>{{Audio}}'
            },
        ])

    anki_deck = genanki.Deck(
        2059400110,
        'Language Subtitles')

    for val in cardArray:
        convertTextToMp3(val['back'])
        audioFileName = '[sound:{}.mp3]'.format(val["back"].replace(" ", "_"))
        print(audioFileName)
        anki_note = genanki.Note(
            model=anki_model,
            fields=[val["front"], val["back"], audioFileName])
        anki_deck.add_note(anki_note)

    my_package = genanki.Package(anki_deck)

    mediaArray = []
    for val in cardArray:
        mediaArray.append('./audio/' + val["back"].replace(" ", "_") + '.mp3')

    my_package.media_files = mediaArray
    my_package.write_to_file('output.apkg')
