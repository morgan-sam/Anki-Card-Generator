import re
import spacy


def removeCommas(string):
    return string.replace(',', '')


def removeNumericCommas(str):
    return re.sub(r'[0-9]+(?:\,[0-9]+)+',
                  lambda x: removeCommas(x[0]), str)


def extractSentencesFromText():
    sentences = []
    file = open('text.txt')
    doc = file.read()
    nlp = spacy.load('en_core_web_sm')
    tokens = nlp(doc)
    for sent in tokens.sents:
        sentences.append(sent.string.strip())
    return sentences
