
from googletrans import Translator


def listToCardArray():
    translator = Translator()
    translations = []
    filepath = 'Sentences.txt'
    with open(filepath) as fp:
        for line in enumerate(fp):
            entry = {"front": line[1], "back": translator.translate(
                line[1], dest='es').text}
            translations.append(entry)
    print(translations)
    return translations
