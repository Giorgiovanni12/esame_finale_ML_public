'''Creazione del Database'''
import sqlite3
import pandas as pd


#Creazione del dataset e connessione a sqlite
ds = pd.read_csv(
"https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/shopping_trends.csv")
connection = sqlite3.connect('Shopping.sqlite')


#Creazione del DB , aggiungi un campo ID da usare per la ricerca e modifica del campo frequenza
ds.replace("Weekly","One Week",inplace=True)
ds.insert(0, 'ID', range(0, 0 + len(ds)))
ds.to_sql(name="Shopping",con=connection)
ds.info()
ds.count()
#stampa di alcune informazioni a schermo come type delle colonne e utilizzo di memoria
