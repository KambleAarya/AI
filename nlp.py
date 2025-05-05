Practical 9

Code:
# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import asyncio
from textblob import TextBlob
from langdetect import detect
from googletrans import Translator
from autocorrect import Speller

# Step 1: Load text data
text = ''' 
        I went through Mrs Shears’ gate, closing it behind me. I walked onto her lawn and knelt beside the dog. I put my hand on the muzzle of the dog. It was still warm. 
'''
# Step 2: Tokenize text
words = word_tokenize(text)
sentences = sent_tokenize(text)
# Step 3: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
# Step 4: Apply stemming or lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
# Step 5: Perform POS tagging
pos_tags = pos_tag(lemmatized_words)
# Step 6: Apply Named Entity Recognition (NER)
# Using TextBlob for simplicity
blob = TextBlob(text)
named_entities = blob.tags
# Step 7: Normalize text
normalized_text = text.lower()

# Step 8: Convert text to numerical format
# Using TF-IDF for simplicity
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform([normalized_text])
# Step 9: Perform sentence tokenization
sentences = sent_tokenize(text)
print("\nSentence Tokenization:")
print(sentences)
# Step 10: Count word frequency
# Using CountVectorizer for simplicity
count_vectorizer = CountVectorizer()
word_freq = count_vectorizer.fit_transform([normalized_text])
# Step 11: Create Bag of Words (BOW) representation
vectorizer = CountVectorizer()
bow_representation = vectorizer.fit_transform([text])
# Step 12: Perform sentiment analysis
# Using TextBlob for simplicity
sentiment = blob.sentiment
# Step 13: Detect language
language = detect(text)
# Step 14: Translate text
async def translate_text(text):
    translator = Translator()
    result = await translator.translate(text, dest='es')
    return result.text

translated_text = asyncio.run(translate_text(text)) # Translate to Spanish
# Step 15: Apply spelling correction
spell = Speller()
corrected_text = spell(text)
# Print the results
print("Original Text:")
print(text)
print("\nTokenized Words:")
print(words)
print("\nTokenized Sentences:")
print(sentences)
print("\nFiltered Words (Stopwords Removed):")
print(filtered_words)
print("\nLemmatized Words:")
print(lemmatized_words)
print("\nPOS Tags:")
print(pos_tags)
print("\nNamed Entities:")
print(named_entities)
print("\nNormalized Text:")
print(normalized_text)
print("\nTF-IDF:")
print(tfidf.toarray())
print("\nWord Frequency:")
print(word_freq.toarray())
print("\nBag of Words (BOW) Representation:")
print(bow_representation.toarray())
print("\nSentiment Analysis:")
print(sentiment)
print("\nLanguage Detection:")
print(language)
print("\nTranslated Text (Spanish):")
print(translated_text)
print("\nCorrected Text (Spelling Correction):")
print(corrected_text)


Output:






