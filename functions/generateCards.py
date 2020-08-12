import re
import genanki


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
                'qfmt': '<div style="display: flex; justify-content: center;"><h2>{{Target}}</h2></div>',
                'afmt': '{{FrontSide}}<hr id="answer"><div style="display: flex; flex-direction: column; align-items: center;"><h2>{{Source}}</h2>{{Audio}}</div>'
            },
        ])

    anki_deck = genanki.Deck(
        2059400110,
        'Language Subtitles')

    for val in cardArray:
        anki_note = genanki.Note(
            model=anki_model,
            fields=[val["front"], val["back"], '[sound:{}]'.format(val["audio"])])
        anki_deck.add_note(anki_note)

    my_package = genanki.Package(anki_deck)

    mediaArray = []
    for val in cardArray:
        mediaArray.append('./audio/' + val["audio"])

    my_package.media_files = mediaArray
    my_package.write_to_file('output.apkg')
