import spacy
# from spacy import displacy
nlp = spacy.load("ru_core_news_lg")

def get_annotations(text):
    doc = nlp(text)
    return {"text":text, "label":[
        [ent.start_char, ent.end_char, ent.label_]
        for ent in doc.ents
    ]}


# displacy.serve(doc, style="ent")

