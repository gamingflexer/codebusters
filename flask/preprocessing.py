import re,emoji
from bs4 import BeautifulSoup

def clean_text(text):
    try:
        '''Clean emoji, Make text lowercase, remove text in square brackets,remove links,remove punctuation
        and remove words containing numbers.'''
        text = emoji.demojize(text)
        text = re.sub(r'\:(.*?)\:', '', text)
        text = str(text).lower()  # Making Text Lowercase
        text = re.sub('\[.*?\]', '', text)
        # The next 2 lines remove html text
        text = BeautifulSoup(text, 'lxml').get_text()
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",", "'")
        text = re.sub(r"[^a-zA-Z?.!,¿']+", " ", text)
        return text
    except:
        return text