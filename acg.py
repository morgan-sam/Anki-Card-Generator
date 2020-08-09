from functions.generateCards import generateDeck
from functions.listConversion import listToCardArray
from functions.subtitlesConversion import subtitlesToCardArray
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
SECRET_KEY = os.environ.get("SECRET_KEY")
print(SECRET_KEY)

# cardArray = subtitlesToCardArray()
cardArray = listToCardArray()
# generateDeck(cardArray)
