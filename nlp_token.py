import nltk
import sklearn

paragraph = "Although the vast majority of cases have been in China, the virus, which can cause pneumonia, is worrying global health authorities. Dozens of cases have been confirmed in 24 countries, and two deaths have been recorded outside of China (in Japan and the Philippines). Most of those affected by the virus had travelled from Wuhan, the epicentre of the outbreak."
sentence = nltk.sent_tokenize(paragraph)
word = nltk.word_tokenize(paragraph)
print(sentence)
print(word)