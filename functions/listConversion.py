
from googletrans import Translator


def listToCardArray():
    translator = Translator()
    translations = []
    filepath = 'Sentences.txt'
    with open(filepath) as fp:
        for line in enumerate(fp):
            translations.append(translator.translate(line[1], dest='es').text)
    print(translations)
