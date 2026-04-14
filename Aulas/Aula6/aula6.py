import spacy


nlp = spacy.load("pt_core_news_sm")

text = "O gato comeu a sardinha do Luís nas ruas de Braga."

doc = nlp(text)

for token in doc:
    print(token.text, " POS:",token.pos_, " Lemma:", token.lemma_, " Dep:", token.dep_, " Entity: ", token.ent_type_, " Head: ", token.head.text, " Morph: ", token.morph)



for ent in doc.ents:
    print(ent, ent.label_)

for sent in doc.sents:
    print(sent)

from spacy import displacy

displacy.serve(doc, style="ent") # dep
