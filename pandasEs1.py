"""
Creare un dataframe e stamparlo avendo come fonte l’XML utilizzato perl’esercizio sui libri:
<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>
"""

import pandas as pd
import xml.etree.ElementTree as ET

xml = """<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>
"""

root = ET.fromstring(xml)

df_col = ["titolo", "autore"]
df_row = []

for nodo in root:
    titolo = nodo.find('titolo').text if nodo is not None else None
    autore = nodo.find('autore').text if nodo is not None else None

    df_row.append({"titolo":titolo, "autore":autore})

df = pd.DataFrame(df_row, columns=df_col)
print(df)
print("\n")

df.to_csv("libri.csv", index=False)
df.to_html("libri.html", index=False)



