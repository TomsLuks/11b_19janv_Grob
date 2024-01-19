import json 

#nolasīt JSON failu
with open('1.uzd.json', 'r', encoding='utf-8') as tt:
    dati=json.load(tt)

    print(dati["koki"])
      