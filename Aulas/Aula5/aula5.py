import json

f = open("../Aula4/dicionario_medicina.json")

dados = json.load(f)

markdown = """
---
title: Dicionário Médico PT
author:
    - SPLN2526
    - Universidade do Minho
classoption: twocolumn
---
"""


for conceito in dados:
    markdown += f"## {conceito} {dados[conceito]['pt']}\n"
    if "dom" in dados[conceito]:
        markdown += dados[conceito]["dom"] + "\n"
    if "sin" in dados[conceito]:
        markdown += dados[conceito]["sin"] + "\n"
    if "var" in dados[conceito]:
        markdown += dados[conceito]["var"] + "\n"
    if "es" in dados[conceito]:
        markdown += f"Espanhol:  {dados[conceito]['es']}\n"
    if "en" in dados[conceito]:
        markdown += f"Ingles:  {dados[conceito]['en']}\n"
    if "la" in dados[conceito]:
        markdown += f"Latim:  {dados[conceito]['la']}\n"
    if "ga" in dados[conceito]:
        markdown += f"Galego:  {dados[conceito]['ga']}\n"
    if "notas" in dados[conceito]:
        markdown += f"Notas:  {dados[conceito]['notas']}\n"
    markdown += "\n\n"



f_out = open("dicionario.md","w")
f_out.write(markdown)