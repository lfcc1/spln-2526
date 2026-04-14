import spacy
from collections import Counter

nlp = spacy.load("pt_core_news_sm")

f = open("../../Dados/Harry Potter e A Pedra Filosofal.txt")

texto = f.read()
doc = nlp(texto)

res = Counter()
for token in doc:
    if token.pos_ in ["VERB","AUX"] and not token.is_stop:
        if token.lemma_ not in res:
            res[token.lemma_] = 1
        else:
            res[token.lemma_] += 1

#sorted_res = sorted(res.items(), key=lambda x: x[1])
#print(sorted_res[-10::-1])

print(res)


