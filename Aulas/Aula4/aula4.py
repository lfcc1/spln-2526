#ler o ficheiro
import re
f = open("medicina.txt", encoding ="utf8")
texto = f.read()


#marcar conceitos
texto = re.sub(r"\n(\d+) ", r"\n@\1 ", texto)

# extrair conceitos

conceitos = re.split("@", texto)


def processar_conceito(c):
    #marcar elementos
    c = re.sub(r"SIN\.-",r"@SIN.-", c)
    c = re.sub(r"VAR\.-",r"@VAR.-", c)
    c = re.sub(r"Nota\.-",r"@Nota.-", c)

    c = re.sub(r"\n(en|pt|es|la) ", r"\n#\1 ", c)
    
    print(c)
    #### extrair
    id = re.search(r"^(\d+) ", c)
    sin = re.search(r"@SIN\.-([^@#]+)", c)
    var = re.search(r"@VAR\.-([^@#]+)", c)
    nota = re.search(r"@Nota\.-([^@#]+)", c)
    langs = re.findall(r"#(la|es|en|pt) ([^#@]+)", c)
    print(c)
    ga_dom = re.search(r"^\d+\s*(.*)\n(.*)", c)
    ga = ga_dom.group(1)
    dom = ga_dom.group(2)
    res = {}

    if nota:
        res["nota"] = nota.group(1)
    if var:
        res["var"] = var.group(1)
    if sin:
        res["sin"] = sin.group(1)
    
    res["dom"] = dom
    res["ga"] = ga
    for l, t in langs:
        res[l] = t
    return res, id.group(1)

entries = {}
for c in conceitos[1:]:
    res, id = processar_conceito(c)
    entries[id] = res

import json
f_out = open("dicionario_medicina.json","w", encoding="utf8")
json.dump(entries, f_out, indent=4, ensure_ascii=False)
#print(conceitos)

#print(texto)

