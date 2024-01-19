import csv

def kola(csv1):
        with open(csv1, 'r', encoding='utf-8') as tt:
            tt2 = csv.reader(tt)

            print("Otrās kolonnas dati: ")
            for rinda in tt2:
                if len(rinda) > 1:
                    print(rinda[1])
csv1 = '2uzd.csv'

kola(csv1)