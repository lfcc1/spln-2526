import requests
from bs4 import BeautifulSoup
import json

html_doc = requests.get("https://www.atlasdasaude.pt/doencasaaz/a")

soup = BeautifulSoup(html_doc.text, 'html.parser')

#print(soup)

doencas_div = soup.find_all("div", class_="views-row")

res = {}

for div in doencas_div:
    designacao = div.div.h3.a.text
    descricao = div.find("div", class_="views-field-body").div.text
    res[designacao] = descricao.strip()


f_out = open("doencas.json", "w")
json.dump(res, f_out, indent= 4, ensure_ascii= False)

# <div class="views-row views-row-30 views-row-even views-row-last">
#     <div class="views-field views-field-title"> 
#         <h3 class="field-content">
#             <a href="/content/aterosclerose">Aterosclerose</a>
#         </h3> 
#     </div>
#     <div class="views-field views-field-body"> 
#         <div class="field-content"> 
#             <p>Aterosclerose é um termo geral que designa várias doenças nas quais se verifica espessamento e perda de elasticidade da parede arterial.
#             </p>
#         </div> 
#     </div> 
# </div>