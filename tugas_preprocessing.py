import string
import matplotlib.pyplot as plt
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

# 1. Download resource NLTK dasar
nltk.download('punkt')
nltk.download('stopwords')

# 2. Baca file CSV
file_path = r'Github_Pemteks\Tugas_Pemrosesan_teks\produk_oxylabs.csv'
df = pd.read_csv(file_path)

# Inisialisasi PorterStemmer dan Stopwords
porter = PorterStemmer()
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
  if not isinstance(text, str):
    return ''

  # Lowercase & Hapus Punctuation
  text = text.lower().translate(str.maketrans('', '', string.punctuation))

  # Tokenisasi
  tokens = word_tokenize(text)

  # Hapus Stopwords + Simple Stemming dengan Porter
  cleaned = [
      porter.stem(word)
      for word in tokens
      if word not in stop_words and len(word) > 2
  ]

  return ' '.join(cleaned)


# 3. Terapkan ke DataFrame
df['Deskripsi_Clean'] = df['Deskripsi'].apply(preprocess_text)

# 4. WordCloud
text_combined = ' '.join(df['Deskripsi_Clean'])
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    max_words=100,
).generate(text_combined)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud (Porter Stemmer NLTK)', fontsize=14, pad=15)
plt.tight_layout()
plt.show()