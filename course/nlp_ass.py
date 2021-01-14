import pdfplumber
from gensim import corpora, models
import spacy

pdf = pdfplumber.open('../data/text.pdf')
nlp = spacy.load('en_core_web_sm')
all_texts = []
for pid in range(len(pdf.pages)):
    text = pdf.pages[pid].extract_text()
    all_texts.append([word for word in text.split(' ')])

# bag of word analysis
dictionary = corpora.Dictionary(all_texts)
corpus = [dictionary.doc2bow(text) for text in all_texts]
print(corpus)

# NER analysis
for text in all_texts:
    doc = nlp(' '.join(text))
    for x in doc.ents:
        print(x.text, x.label_)

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)
