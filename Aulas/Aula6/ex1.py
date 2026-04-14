import spacy

nlp = spacy.load("pt_core_news_sm")



texto = """Se calhar, aquilo que é preciso refletir é se faz sentido numa escola termos os dois regimes (oferta privada e contratos de associação). Eu diria que essa é que pode ser a questão", afirmou Fernando Alexandre.

A hipótese de repensar os contratos de associação foi lançada pelo ministro da Educação, Ciência e Inovação quando questionado sobre o caso, noticiado pela Lusa na sexta-feira, de um colégio onde os alunos do regime público e privado têm acessos diferenciados às refeições da cantina.

No colégio em causa - Salesianos de Manique, em Cascais - há 770 alunos em regime privado, que pagam mensalidades, e 797 que frequentam a escola gratuitamente porque o Ministério da Educação financia estas turmas, por falta de oferta da rede pública."""


doc = nlp(texto)

for ent in doc.ents:
    if ent.label_ in ["PER","ORG"]:
        print(ent, ent.label_)
