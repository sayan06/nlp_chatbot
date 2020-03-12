import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = "Although the vast majority of cases have been in China, the virus, which can cause pneumonia, is worrying global health authorities. Dozens of cases have been confirmed in 24 countries, and two deaths have been recorded outside of China (in Japan and the Philippines). Most of those affected by the virus had travelled from Wuhan, the epicentre of the outbreak."
sentences = nltk.sent_tokenize(paragraph)
stemmer   = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    #sentences[i] = ' '.join(words)
    print(words)
