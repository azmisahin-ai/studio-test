import spacy
# python -m spacy download "en_core_web_sm"
def process_text(txt):
    # spaCy modelini yükle
    nlp = spacy.load("en_core_web_sm")

    # Metni işle
    doc = nlp(txt)

    # Cümleleri listele
    cumleler = [str(cumle) for cumle in doc.sents]

    return cumleler