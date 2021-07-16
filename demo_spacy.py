import spacy
nlp = spacy.load("es_dep_news_trf")

def spacy_info(text):
    doc = nlp(text)
    print([(w.text, w.pos_) for w in doc])
    return doc

if __name__ == '__main__':
    item = "Holi hermosa señorita"
    doc = spacy_info(item)
    for w in doc:
        print(w.text, w.pos_)