# Progetto NoLimit Math
Il progetto "NoLimit Math" è sviluppato in Python, con GUI PyQt5.
Il progetto è incentrato sul calcolo automatizzato di limiti (come (ax^2+bx+c)/(ax^2+bx+c)), finiti, infiniti o indeterminati (forma indeterminata calcolata: ∞/∞) e generazione del grafico relativo.
NoLimit Math è nato, principalmente, come progetto per la "tesina" degli esami di maturità: INFORMATICA applicata alla MATEMATICA, al concetto di limite.

## Script Python
Lo script Python principale è "main.py", presente nella cartella "File"

## Come funziona
E' possibile inserire un numeratore, del tipo "ax^2+bx+c" (dove a, b e c siano numeri). Può essere anche inserito uno solo di quelli, quindi "ax^2"/"bx"/"c" oppure solo 2 di essi "ax^2+bx"/"bx+c"/"ax^2+c".
Il denominatore sarà uguale al numeratore. di default ha valore "1", quindi come se non ci fosse.
Il programma restituisce un errore in caso di denominatore "0".

Inserire poi il valore x0 a cui far tendere la x nell'apposita casella di testo.

Successivamente premere il pulsante "Calcola e genera grafico" per ottenere il risultato finale e il grafico.
**IL GRAFICO NON E' DISPONIBILE ATTUALMENTE**
## Screenshots
Sono presenti alcuni screenshots nella cartella "Screenshot"

## PROGETTO REALIZZATO DA SAVERIO MORELLI
## LICENZA GNU v3, leggere file LICENSE

## Librerie utilizzate
- PyQt5
- Matplot
