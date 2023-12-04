Unità Formativa (UF): Data Analytics e Machine Learning
Docente: Fabio Giuseppe Antonio Gagliardi
Titolo argomento: esame
Commentare i passaggi importanti. Nello specifico:
a cosa serve un blocco di codice, una classe o una funzione
motivare le scelte effettuate nel codice.
L'ASSENZA DI COMMENTI SARÀ VALUTATA NEGATIVAMENTE
QUALORA DUE O PIÙ PROVE DOVESSERO RIPORTARE GLI STESSI COMMENTI E LO STESSO CODICE, SARANNO TUTT VALUTATE
CON IL VOTO MINIMO.
es.
Si è liberi di utilizzare qualisasi strumento per rispondere alle richieste.
Non è consentito il copia-incolla da chatgpt. Qualora i test di controllo dovessero confermarne l'uso, l'eame verrà valutato direttamente
con voto mininmo.
REGOLE ESAME
Il dataset aggreta dei report provenienti da un E-commerce
https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/shopping_trends.csv
DATI
Il progetto è diviso in tre moduli e deve essere consegnato seguendo lo schema delle cartelle indicato di seguito.
PROGETTO
cartella_progetto
|
|-cartella_database
| |
| |-cartella_sqlite
| | |-db.sqlite
| |-db.py
| |-api.py
|
|-cartella_statistiche
| |-stat_api.py
|
|-cartella_classificazione
| |-cls_api.py
N.B Nomi di file e cartelle utilizzati nell'esempio sono solo a scopo descrittivo. La scelta della nomenclatura è a discrezione dello studente,
purché sia pertinente al progetto e rispetti lo schema.
Schema
I primi due moduli sono obbligatori, il terzo è facoltativo
Moduli
Cosa fare:
impostare un database a partire dai dati forniti.
implementare le operazioni CRUD (Create, Read, Update, Delete)
creazione di API REST
Sviluppo:
python + sqlite.
Cosa verrà valutato:
l'organizzazione e stesura del codice
la progettazione del database
il corretto funzionamento di tutti gli endpoint da swagger
2. Modulo Database
Cosa fare:
Calcolare la media dell'età degli acquirenti (colonna Age)
Calcolare la spesa media effettuata sull' e-commerce (colonna Purchase Amount)
Calcolare la mediana delle spese precedenti (colonna Previous Purchases)
Calcolare come sono divise in percentuale le frequenze di acquisto (colonna Frequency of Purchases)
creazione di API REST su ognuna delle precedenti richieste
Sviluppo:
python.
Cosa verrà valutato:
l'organizzazione e stesura del codice
il corretto funzionamento di tutti gli endpoint da swagger
3. Modulo Statistiche
In questo modulo si chiede di estenedere la capacità del progetto alla gestione dell'usato tramite immagini.
Cosa fare:
Estendere il modello di classificazione YoloV8 con il dataset OpenImageV7.
Salvare il risultato e riutilizzare il nuovo modello all'interno del progetto.
Implementare un'api rest con la funzionalità di prendere un'immagine, classificarla e se è un capo di abbigliamento salvarla in un apposita
cartella
