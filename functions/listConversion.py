
from googletrans import Translator


def listToCardArray():
    translator = Translator()
    translations = []
    file = open('Sentences.txt')
    for line in file.read().splitlines():
        sentence = (' '.join(line.split()))
        if sentence.endswith('.'):
            sentence = sentence[:-1]
        translation = translator.translate(sentence, dest='es').text
        entry = {"front": sentence, "back": translation}
        translations.append(entry)
    return translations
