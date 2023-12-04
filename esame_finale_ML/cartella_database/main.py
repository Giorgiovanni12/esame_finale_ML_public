'''Api per operazioni CRUD sul database Shopping'''
import sqlite3
from fastapi import FastAPI,HTTPException
import uvicorn

#crea connessione a sqlite e un cursore per effettuare le operazioni sul DB
connection = sqlite3.connect('esame_finale_sello_giovanni/cartella_database/Shopping.sqlite',check_same_thread=False)
cursor=connection.cursor()



app = FastAPI()


@app.get("/")
async def root():
    '''Prova'''
    return {"Prova": "Benvenuto <3"}

@app.get("/get")
async def getall():
    '''GET ALL'''
    #get di tutti gli elementi della tabella Shopping
    cursor.execute("Select * from Shopping")
    #ritorna tutti gli elementi
    result=cursor.fetchall()
    #devo trasformare tutti i risultati in JSON sennò non vedo i nomi delle tabelle
    columns = [column[0] for column in cursor.description]
    result_list = [dict(zip(columns, row)) for row in result]
    return result_list

@app.get('/get/{ID}')
def get_data_by_id(ID):
    '''Get by ID'''
    # Esegui una query per recuperare i dati con l'ID specificato
    
    cursor.execute("SELECT * FROM Shopping WHERE ID = ?", [ID])
    #ritorna solo il campo richiesto
    result = cursor.fetchone()

    if result is not None:
        columns = [column[0] for column in cursor.description]
        result_dict = dict(zip(columns, result))
        return result_dict

    else :
        raise HTTPException(status_code=404, detail="Item not found")

@app.post('/crea')
def insert_data(ID,customer_id,age,gender,item_purchased,category,
purchase_amount,location,size,color,season,review_rating,subscription_status,payment_method,
shipping_type,discount_applied,promo_code_used,previous_purchases,preferred_payment_method,
frequency_of_purchases):
    '''POST'''
    #passaggio di tutti i parametri nel body come obbligatori
    cursor.execute('''INSERT INTO Shopping (ID,
    "Customer ID", Age, Gender, "Item Purchased", Category, 
    "Purchase Amount (USD)", Location, Size, Color, Season, 
    "Review Rating", "Subscription Status", "Payment Method", "Shipping Type", 
    "Discount Applied", "Promo Code Used", "Previous Purchases", 
    "Preferred Payment Method", "Frequency of Purchases" )
    
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',

    [ID,customer_id,age,gender,item_purchased,category,
    purchase_amount,location,size,color,season,review_rating,subscription_status,payment_method,
    shipping_type,discount_applied,promo_code_used,previous_purchases,preferred_payment_method,
    frequency_of_purchases])
    #commit per salvare le modifiche
    connection.commit()

    return 'Inserito correttamente'

@app.put('/update/{ID}')
def put_data(ID,customer_id,age,gender,item_purchased,category,
purchase_amount,location,size,color,season,review_rating,subscription_status,payment_method,
shipping_type,discount_applied,promo_code_used,previous_purchases,preferred_payment_method,
frequency_of_purchases):
    '''UPDATE'''
    #Passaggio di tutti i parametri per l'update
    update_query = f'''UPDATE shopping SET
    "Customer ID" = '{customer_id}',
    Age = '{age}',
    Gender = '{gender}',
    "Item Purchased" = '{item_purchased}',
    Category = '{category}',
    "Purchase Amount (USD)" = '{purchase_amount}',
    Location = '{location}',
    Size = '{size}',
    Color = '{color}',
    Season = '{season}',
    "Review Rating" = '{review_rating}',
    "Subscription Status" = '{subscription_status}',
    "Payment Method" = '{payment_method}',
    "Shipping Type" = '{shipping_type}',
    "Discount Applied" = '{discount_applied}',
    "Promo Code Used" = '{promo_code_used}',
    "Previous Purchases" = '{previous_purchases}',
    "Preferred Payment Method" = '{preferred_payment_method}',
    "Frequency of Purchases" = '{frequency_of_purchases}'
    WHERE ID = '{ID}' '''

    #eseguiamo la query di sqlite e salviamo le modifiche
    cursor.execute(update_query)
    connection.commit()

    return("Modificato")

@app.delete('/delete/{ID}')
def delete_data(ID):
    '''DELETE'''
    cursor.execute("DELETE FROM Shopping WHERE ID = ?", [ID])
    connection.commit()
    if cursor.rowcount > 0:
        return {"il record con l'ID:{ID} è stato eliminato con successo"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


#run dell'applicazione sulla porta 8000

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

