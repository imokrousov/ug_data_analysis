import numpy as np

text_data1 = ['  dsfadsf sadfadsf sdfs!',
              'dsafadsg adsfs',
            '    df        sadsf dfs']
short_text_data1 = [string.strip() for string in text_data1]
print(short_text_data1)
bez_a = [string.replace("a","") for string in text_data1]
print(bez_a)

def my (string : str) -> str :
    return  string.upper()
print([my(string) for string in text_data1])

html = """
        <div id="disqus_thread"> TEXT </div>
        <span class="br0">&#125;</span>
        """

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.find("div").text)

import unicodedata
import sys
text_data2 = [
    "@#@@!$!!HIHIHI!!__))",
    "THE#TWEET",
    "WAT!!????"
]
punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith("P"))
print(punctuation)
print([string.translate (punctuation) for string in text_data2])

string = "Даже путь в тысячу ли начинается с первого шага"

from nltk.tokenize import  word_tokenize

tokens = word_tokenize(string)
print(tokens)

from nltk.tokenize import  sent_tokenize

string = """
Representatives and direct Taxes shall be apportioned among the several States which may be included within this Union, according to their respective Numbers, which shall be determined by adding to the whole Number of free Persons, including those bound to Service for a Term of Years, and excluding Indians not taxed, three fifths of all other Persons. The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to chuse three, Massachusetts eight, Rhode-Island and Providence Plantations one, Connecticut five, New-York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five, and Georgia three."""
for s in sent_tokenize(string): print(s)

import nltk
from nltk.corpus import stopwords
#nltk.download("stopwords")
text_data3 = ['We', 'the', 'People', 'of', 'the', 'United', 'States']
s_word = stopwords.words("english")
print ( [word for word in text_data3 if word not in s_word])
print(s_word)

from nltk.stem.porter import PorterStemmer

tokenized_text4 = word_tokenize("The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature.")
print(tokenized_text4)
ps = PorterStemmer()
bases = [ ps.stem (word) for word in tokenized_text4]
print(bases)

from nltk.stem.snowball import SnowballStemmer
sps = SnowballStemmer("russian")

from  nltk.stem import  WordNetLemmatizer

lexems = ["go",'went', 'gone', 'am','are','were']
lemmatizer = WordNetLemmatizer()

print( [ lemmatizer.lemmatize(word, pos = 'v') for word in lexems])

from nltk import  pos_tag

text = "All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives."
print(pos_tag(word_tokenize(text)))


text_data4 = np.array( [
    'World - you is my love. World',
    "Russia is better",
    "German strikes back"
])
from  sklearn.feature_extraction.text import  CountVectorizer
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data4)
print(bag_of_words.toarray())
print(count.get_feature_names_out())

from  sklearn.feature_extraction.text import  TfidfVectorizer

tfid = TfidfVectorizer()
feature_mat = tfid.fit_transform(text_data4)
print(feature_mat.toarray())
