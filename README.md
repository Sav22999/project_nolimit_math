## PROGETTO DI SAVERIO MORELLI
## LICENZA GNU GPL v3, leggere file LICENSE
#### Tutti i contenuti relativi a questo progetto sono sotto licenza GNU GPL v3, incluso il codice, le immagini e il contenuto.

## Mappa README
- Progetto NoLimit Math - Descrizione del progetto
- Linguaggio di programmazione utilizzato e file principale del progetto
- Come funziona
- Screenshots
- Librerie utilizzate
- Come collaborare
- Collaboratori
- OS su cui è testato il software

# Progetto NoLimit Math
Il progetto "NoLimit Math" è sviluppato in Python, con GUI PyQt5.
Il progetto è incentrato sul calcolo automatizzato di limiti (come (ax^2+bx+c)/(ax^2+bx+c)), finiti, infiniti o indeterminati (forma indeterminata calcolata: ∞/∞) e generazione del grafico relativo.
NoLimit Math è nato, principalmente, come progetto per la "tesina" degli esami di maturità (titolo tesina "Oltre i limiti", IIS settore Informatica): INFORMATICA applicata alla MATEMATICA, al concetto di limite matematico.

## Linguaggio di programmazione utilizzato e file principale del progetto
Il linguaggio utilizzato è il Python(3), e il file principale è "main.py", presente nella cartella "File".
Per poter visualizzare bene il progetto è necessario che l'icona, anch'essa presente nella cartella "File", sia presente nella cartella dello script stesso.

## Come funziona
E' possibile inserire un numeratore, del tipo "ax^2+bx+c" (dove a, b e c siano numeri). Può essere anche inserito uno solo di quelli, quindi "ax^2"/"bx"/"c" oppure solo 2 di essi "ax^2+bx"/"bx+c"/"ax^2+c".
Il denominatore sarà uguale al numeratore. di default ha valore "1", quindi come se non ci fosse.
Il programma restituisce un errore in caso di denominatore "0".

Inserire poi il valore x0 a cui far tendere la x nell'apposita casella di testo.

Successivamente premere il pulsante "Calcola e genera grafico" per ottenere il risultato finale e il grafico.

Se si vuole visualizzare in maniera più accurata il grafico sarà sufficiente premere sul pulsante che compare dopo aver premuto su "Calcola e genera grafico", ovvero "Visualizza grafico nel dettaglio".

## Screenshots
Sono presenti alcuni screenshots del software nella cartella "screenshot"

## Librerie utilizzate
- PyQt5
- Matplotlib
- Sympy (per versione "sympy")

## Come collaborare
Collaborare al progetto è molto semplice: è sufficiente aprire un nuovo issue in caso si vogliano aggiungere nuove funzionalità, successivamente si può procedere alla pr.
Si può collaborare anche solo segnalando un problema o un consiglio.

**NB. Viene effettuato il merge delle pr direttamente (e solamente) da Sav22999.**

## OS su cui è testato il software
Sono stati effettuati differenti test sui seguenti sistemi operativi, sui quali è garantita la compatibilità:
- Kubuntu (18.04)
- Ubuntu (18.04)
- Windows 10 (Home) - presenta alcuni problemi: non apre il grafico dettagliato

## Collaboratori
- Sav22999 - Saverio Morelli
- Mone27 - Simone Massaro
