import requests
import json
import pandas as pd
import sys



def getData(codigo):
    data = {"Authorization":"Token a39b1095be03e6ac7387048b12cc8cdb4d6cd41d"}
    url4 = f"https://kobo.humanitarianresponse.info/api/v2/assets/{codigo}/data/?format=json"
    d =requests.get(url4, headers=data)
    d2 = json.loads(d.text)
    df = pd.DataFrame(d2["results"])
    return df

def proceso():
    fuentes = [["aiT4U8ReXktYenGVzJnXJ7","DataCasen"],["aXPhYrh4SQhqbfMZBj7ZoS","Navidad"]]
    for i in fuentes:
        data = getData(i[0])
        data.to_excel(f"data/{i[1]}.xlsx", index=False)
    return None

if __name__ == '__main__':
    print("Comenzo...")
    proceso()