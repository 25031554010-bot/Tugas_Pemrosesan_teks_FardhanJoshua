import warnings
warnings.filterwarnings(action='ignore')
import re
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from mpstemmer import MPStemmer
stemmer = MPStemmer()
nltk.download('punkt_tab')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
wnl = WordNetLemmatizer()
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem import LancasterStemmer
ls = LancasterStemmer()


text = '''<p class="description css-cput12 eag3qlw5">As a young boy, 
Link is tricked by Ganondorf, the King of the Gerudo Thieves. The evil human uses Link to 
gain access to the Sacred Realm, where he places his tainted #hands on Triforce and transforms 
the beautiful Hyrulean landscape into a barren wasteland. jos@gmail.com
Link is determined to fix the problems he helped to create, so with the help of 
Rauru he travels through time gathering the powers of the Seven Sages https://sandbox.oxylabs.io/products .</p>'''

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)
def remove_hashtag(text):
    return re.sub(r'#\w+', '', text)

hasil_ht = remove_html(text)
# print(hasil_ht)

result = remove_hashtag(hasil_ht)
# print(result)

hasil_cf = str.lower(result)
# print(hasil_cf)

def remove_rls(text):
    text = re.sub(r'https?\/\/S+', '',  str(text)) # remove the hyperlink
    text = re.sub(r'http\S+', '',  str(text)) # remove the hyperlink
    text = re.sub(r'www\S+', '',  str(text)) # remove the www
    text = re.sub(r'\S+@\S+', '', str(text)) # remove the email
    return text

hasil_rl = remove_rls(hasil_cf)
print(hasil_rl)


punc = string.punctuation

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punc))

hasil_rp = remove_punctuation(hasil_rl)
print(hasil_rp)

def remove_punctuation_list(text):
    # List Emoticon
    text = re.sub(r'(:\)|:-\)|:D|:-D|;\)|;-\))', '', text)
    text = re.sub(r'(:\(|:-\()', '', text)
    text = re.sub(r'(:v|:-v)', '', text)

    # remove punctuation
    text = re.sub(r'[!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text

import demoji
#demoji.download_codes() # Download emoji codes (run once)

def remove_emoji(text):
    cleaned_text = demoji.replace(text,repl="") # Replaces emojis with an empty string
    #cleaned_text = demoji.replace_with_desc(text) # Replaces emojis with text
    return cleaned_text

hasil_rem = remove_emoji(hasil_rp)
print(hasil_rem)


print(stopwords.words('english'))
# print(stopwords.words('indonesian'))

sw = set(stopwords.words('english'))
def remove_stopwords(text):

  return " ".join([word for word in str(text).split() if word not in sw])

hasil_st = remove_stopwords(hasil_rem)
print(hasil_st)

# print(stemmer.stem('mengemudi')) # => kemudi
# print(stemmer.stem('belajar')) # => ajar
# print(stemmer.stem('ngelepas')) # => lepas
# print(stemmer.stem('kebayang')) # => bayang

# print(stemmer.stem_kalimat('ngelupain mantan tuh ngga susah kok bro'))
# # => lupa mantan itu tidak susah kok bro

# from nltk.stem import LancasterStemmer
# ls = LancasterStemmer()
# ls.stem('jumping'), ls.stem('jumps'), ls.stem('jumped'), ls.stem('lying'), ls.stem('strange')
# => ('jump', 'jump', 'jump', 'lying', 'strange')

hasil=ls.stem(hasil_st)
print(hasil)
# from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')
# wnl = WordNetLemmatizer()
# lemmatize nouns
print(wnl.lemmatize('cars', 'n'), wnl.lemmatize('men', 'n'))
print(wnl.lemmatize('running', 'v'), wnl.lemmatize('ate', 'v'))
print(wnl.lemmatize('saddest', 'a'), wnl.lemmatize('fancier', 'a'))

# sentence = 'The brown fox is quick and he is jumping over the lazy dog'
# # nltk.download('punkt_tab')
# # nltk.download('wordnet')
# tokens = nltk.word_tokenize(sentence)
# print(tokens)

hasil1=wnl.lemmatize(hasil)
hasil2=nltk.word_tokenize(hasil)
tokens_st = nltk.word_tokenize(hasil_st)

# 2. Lakukan stemming untuk setiap kata menggunakan list comprehension
stemmed_tokens = [ls.stem(word) for word in tokens_st]

# 3. Gabungkan kembali menjadi string kalimat (jika dibutuhkan untuk WordCloud)
hasil_stemmed = " ".join(stemmed_tokens)
print(hasil_stemmed)


# df = pd.read_csv('https://raw.githubusercontent.com/rizalespe/Dataset-Sentimen-Analisis-Bahasa-Indonesia/refs/heads/master/dataset_tweet_sentiment_cellular_service_provider.csv')
# df.rename(columns={'Text Tweet': 'text'}, inplace=True)
# df.head()
# text = ' '.join(df['text'].dropna().astype(str))

wordcloud = WordCloud(width=1000, height=500, background_color='white', max_words=500).generate(hasil_st)

plt.figure(figsize=(7, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# hasil2['rm_html'] = hasil2['text'].apply(remove_html)
# hasil2['rm_hashtag'] = hasil2['rm_html'].apply(remove_hashtag)
# hasil2[['rm_html','rm_hashtag']].head()
# hasil2['lower_case'] = hasil2['rm_hashtag'].str.lower()
# hasil2[['rm_hashtag', 'lower_case']]
# hasil2['rm_url'] = hasil2['lower_case'].apply(remove_rls)
# hasil2[['lower_case','rm_url']]
# hasil2['rm_punc'] = hasil2['rm_url'].apply(remove_punctuation_list)
# hasil2[['rm_url','rm_punc']]
# hasil2['rm_punc'] = hasil2['rm_url'].apply(remove_punctuation_list)
# hasil3=hasil2[['rm_url','rm_punc']]

# sw = set(stopwords.words('indonesian'))
# def remove_stopwords(text):
#   return " ".join([word for word in str(text).split() if word not in sw])
# df['rm_stopwords'] = df['stem'].apply(remove_stopwords)
# df[['stem','rm_stopwords']]

# text = ' '.join(df['rm_stopwords'].dropna().astype(str))

wordcloud = WordCloud(width=1000, height=500, background_color='white', max_words=100).generate(hasil_stemmed)

plt.figure(figsize=(7, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()