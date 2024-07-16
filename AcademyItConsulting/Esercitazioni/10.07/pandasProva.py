import pandas as pd
import xml.etree.ElementTree as ET

xml = """<data>
<student name="John">
<email>john@mail.com</email>
<grade>A</grade>
<age>16</age>
</student>
<student name="Alice">
<email>alice@mail.com</email>
<grade>B</grade>
<age>17</age>
</student>
<student name="Bob">
<email>bob@mail.com</email>
<grade>C</grade>
<age>16</age>
</student>
<student name="Hannah">
<email>hannah@mail.com</email>
<grade>A</grade>
<age>17</age>
</student>
</data>
"""

root = ET.fromstring(xml)

df_col = ["nome", "email", "grado", "eta"]
df_row = []

for nodo in root:
    nome = nodo.attrib.get("name")  #direttamente al valore
    mail = nodo.find("email").text  if nodo is not None else None #tag
    grado = nodo.find("grade").text if nodo is not None else None
    eta = nodo.find("age").text if nodo is not None else None

    df_row.append({"nome":nome, "email":mail, "grado":grado, "eta":eta})

#print(df_row)

df = pd.DataFrame(df_row, columns=df_col)

print(df)

#df.to_csv("studenti.csv", index=False)   #index True ritorna gli indici degli elementi

#df = pd.read_csv("studenti.csv")    #leggere csv
#print(df)
