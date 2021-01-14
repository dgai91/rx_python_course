import pdfplumber
from gensim import corpora, models
import spacy


pdf = pdfplumber.open('../data/text.pdf')
nlp = spacy.load('en_core_web_sm')
all_texts = []

for pid in range(len(pdf.pages)):
    text = pdf.pages[pid].extract_text()
    text = text.replace('-\n', '').replace('\n', '')
    doc = nlp(text)
    all_texts.append([word.lemma_ for word in doc])
    for x in doc.ents:
        print(x.text, x.label_)
# bag of word analysis
dictionary = corpora.Dictionary(all_texts)
corpus = [dictionary.doc2bow(text) for text in all_texts]
for key in dictionary:
    print(dictionary[key])
# tfidf = models.TfidfModel(corpus)
# corpus_tfidf = tfidf[corpus]
# for doc in corpus_tfidf:
#     print(doc)
