from bs4 import BeautifulSoup
from functions.generateCards import generateDeck
from functions.listConversion import listToCardArray
from functions.subtitlesConversion import subtitlesToCardArray
from functions.extractParagraphSentences import extractParagraphSentences

# cardArray = subtitlesToCardArray()
# cardArray = listToCardArray()
# generateDeck(cardArray)

extractParagraphSentences()
