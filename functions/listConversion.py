
from googletrans import Translator
from functions.convertTextToMp3 import convertTextToMp3


def listToCardArray():
    translator = Translator()
    translations = []
    file = open('Sentences.txt')
    for line in file.read().splitlines():
        sentence = (' '.join(line.split()))
        if sentence.endswith('.'):
            sentence = sentence[:-1]
        translation = translator.translate(sentence, dest='es').text
        convertTextToMp3(translation)
        audioFileName = '{}.mp3'.format(translation.replace(" ", "_"))
        entry = {"front": sentence, "back": translation, "audio": audioFileName}
        translations.append(entry)
    return translations
