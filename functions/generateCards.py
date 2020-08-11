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
        convertTextToMp3(val['back'])
        anki_note = genanki.Note(
            model=anki_model,
            fields=[val["front"], val["back"]])
        anki_deck.add_note(anki_note)

    genanki.Package(anki_deck).write_to_file('language_subtitles.apkg')
