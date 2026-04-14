import spacy
from spacy.matcher import Matcher

f = open("../../Dados/Harry Potter e A Pedra Filosofal.txt")
texto = f.read()

nlp = spacy.load("pt_core_news_sm")
doc = nlp(texto)

matcher = Matcher(nlp.vocab)

pattern = [
  {"ENT_TYPE": "PER", "OP": "+"},
  {"POS": {"IN": ["AUX", "VERB"]}},
  {"POS": "DET", "OP": "?"},
  {"POS": {"IN":["NOUN","PROPN"]}, "OP": "+"}
]

matcher.add("triplos_match", [pattern], greedy="LONGEST")

matches = matcher(doc)

for id, start, end in matches:

    print(doc[start:end])
