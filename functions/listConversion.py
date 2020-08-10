
from googletrans import Translator


def listToCardArray():
    translator = Translator()
    translations = []
    file = open('Sentences.txt')
    for line in file.read().splitlines():
        sentence = (' '.join(line.split()))
        entry = {"front": sentence, "back": translator.translate(
            sentence, dest='es').text}
        translations.append(entry)
    return translations
