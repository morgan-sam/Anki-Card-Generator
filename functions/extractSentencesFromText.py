import re


def removeCommas(string):
    return string.replace(',', '')


def removeNumericCommas(str):
    return re.sub(r'[0-9]+(?:\,[0-9]+)+',
                  lambda x: removeCommas(x[0]), str)


def extractSentencesFromText():
    file = open('text.txt')
    for line in file.read().splitlines():
        line = (' '.join(line.split()))
        if line.endswith('.'):
            line = line[:-1]
        line = removeNumericCommas(line)
        print(re.split('\.|,', line))
