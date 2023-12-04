'''Applicazione per le statistiche'''
import sqlite3
from fastapi import FastAPI
import pandas as pd
import numpy as np
import uvicorn

#connessione al database Shopping
connection = sqlite3.connect('esame_finale_sello_giovanni/cartella_database/Shopping.sqlite',check_same_thread=False)
cursor=connection.cursor()




app = FastAPI()

@app.get("/stats")
async def root():
    '''Prova'''
    return {"Prova": "Benvenuto nelle statistiche"}


@app.get("/age")
async def media_anni():
    '''Media anni
    Calcolare la media dell'età degli acquirenti (colonna Age)'''
    #calcolo della media dell'età direttamente nel DB con AVG()
    cursor.execute("SELECT AVG(AGE) FROM Shopping")
    result=cursor.fetchone()

    #return della media degli acquirenti
    return "Media dell'età degli acquirenti ",result,"Anni"

@app.get("/purchase")
async def media_purchase():
    '''Media degli acquisti
    Calcolare la spesa media effettuata sull' e-commerce  (colonna Purchase Amount)'''
    #calcolo della media sempre con AVG()
    cursor.execute("SELECT AVG([Purchase Amount (USD)]) FROM Shopping")
    result = cursor.fetchone()

    #return del risultato richiesto
    return  "Media delle spese sostenute ",result, "USD$"

@app.get("/previous_purchases")
async def mediana_expurchase():
    '''Mediana degli acquisti
    Calcolare la mediana delle spese precedenti (colonna Previous Purchases)'''
   #uso di numpy median per calcolare la mediana della tabella richiesta
   #Ricreare il dataframe con tutte le informazioni aggiornate
    ds = pd.read_sql_query("SELECT * FROM Shopping",connection)
    mediana_acquisti_precedenti=np.median(ds["Previous Purchases"])

    #return del risultato richiesto
    return "Mediana delle spese sostenute in precedenza", mediana_acquisti_precedenti 


#funzione per calcolare la percentuale di una determinata parola
def calcolapercentuale(parola):
    '''Calcolare la percentuale della parola tra parametro'''
    #viene ricreato un dataset aggiornato all'ultima versione
    ds = pd.read_sql_query("SELECT * FROM Shopping",connection)

    ridondanza = ds["Frequency of Purchases"].str.count(parola).sum()
    #colonne in totale
    totale = len(ds)

    # percentuale
    percentuale = (ridondanza / totale) * 100

    return percentuale



@app.get("/frequency")
async def frequency():
    '''Frequenza degli acquisti con percentuale'''

#Creare variabili con le stringhe per percentuale
    fortinightly=f'''La parola 'Fortnightly' appare nella colonna  Frequency of Purchases {calcolapercentuale("Fortnightly"):.2f}% delle volte.'''
    weekly=f'''La parola 'One Week' appare nella colonna Frequency of Purchases {calcolapercentuale("One Week"):.2f}% delle volte.'''
    biweekly=f'''La parola 'BiWeekly' appare nella colonna Frequency of Purchases {calcolapercentuale("Bi-Weekly"):.2f}% delle volte.'''
    quarterly=f'''La parola 'Quarterly' appare nella colonna Frequency of Purchases {calcolapercentuale("Quarterly"):.2f}% delle volte.'''
    annually=f'''La parola 'Annually' appare nella colonna Frequency of Purchases {calcolapercentuale("Annually"):.2f}% delle volte.'''
    threemonths=f'''La parola 'Every 3 Months' appare nella colonna Frequency of Purchases {calcolapercentuale( "Every 3 Months"):.2f}% delle volte.'''
    monthly=f'''La parola 'Monthly' appare  nella colonna Frequency of Purchases {calcolapercentuale("Monthly"):.2f}% delle volte.'''

   #return di tutti i risultati a schermo
    return fortinightly,weekly,biweekly,quarterly,annually,threemonths,monthly


'''Conta di quante righe ci sono nel db oppure for che conta quanti elementi ci sono dentro
la colonna frequency of purchases
creare un contatore che incrementa di 1 ogni volta
che trova la parola Fortnightly e poi fare Fort/totale *100
nel caso in cui dovessi fare le query sul db
e non sul dataset usare AVG() oppure usare un dataset aggiornato    # pylint: disable=no-member

'''

#run dell'applicazione sulla porta 8000
if __name__ == "__main__":
    uvicorn.run("stat_api:app", host="127.0.0.1", port=8000, log_level="info")
