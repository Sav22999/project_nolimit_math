## PROGETTO DI SAVERIO MORELLI
## LICENZA GNU GPL v3, leggere file LICENSE
#### Tutti i contenuti relativi a questo progetto sono sotto licenza GNU GPL v3 (incluso il codice e le immagini).

- Sito web Saverio Morelli: https://www.saveriomorelli.com/
- Sito web progetto: https://www.saveriomorelli.com/nolimitmath/



## Mappa README
- Progetto NoLimit Math: Descrizione del progetto
- Linguaggio di programmazione utilizzato e file principale del progetto
- Tipi di versioni
- Come funziona
- Screenshots
- Librerie utilizzate
- Come collaborare
- Collaboratori
- OS su cui è testato il software

# Progetto NoLimit Math
Il progetto "NoLimit Math" è sviluppato in Python, con GUI PyQt5.
Il progetto è incentrato sul calcolo automatizzato di limiti finiti, infiniti o indeterminati (forma indeterminata calcolata: ∞/∞) e generazione del grafico relativo.
NoLimit Math è nato, principalmente, come progetto per la "tesina" degli esami di maturità (titolo tesina "Oltre i limiti", IIS settore Informatica): INFORMATICA applicata alla MATEMATICA, al concetto di limite matematico.

## Linguaggio di programmazione utilizzato e file principale del progetto
Il linguaggio utilizzato è il Python(v3.6), e il file principale è "main.py" (in "nolimit)") per la versione Normale e "nolimit\_sympy.py" (in "nolimit">"nolimit\_sympy") per la versione Sympy.
Per poter visualizzare bene il progetto è necessario che l'icona ("icona50x50.png"), anch'essa presente nella cartella "nolimit", sia presente nella cartella dello script stesso.

## Tipi di versioni
Esistono 2 tipi di versione "NORMALE", alle volte "N" o "vN" o "VN" e la versione "SYMPY" che utilizza la libreria Sympy, alle volte "S" o "vS" o "VS".
Entrambe presentano le medesime funzionalità.
La vN è più "macchinosa" non utilizzando la libreria Sympy che permette di effettuare, di fatto, calcoli molto più complessi.
Si consiglia l'utilizzo della versione vN in quanto, da quest'ultima, è possibile aprire anche la vS -> pertanto si avranno "2 versione in un unico programma".

## Come funziona
--- VERSIONE NORMALE ---
E' possibile inserire un numeratore, del tipo "ax^2+bx+c" (dove a, b e c siano numeri). Può essere anche inserito uno solo di quelli, quindi "ax^2"/"bx"/"c" oppure solo 2 di essi "ax^2+bx"/"bx+c"/"ax^2+c".
Se il denominatore è uguale a "1" (valore predefinito) è come se non ci fosse.
Il programma restituisce un errore in caso di denominatore "0" -> ma calcola correttamente il risultato in caso di denominatore "TENDENTE" a 0 (da sinistra e/o destra).

Inserire poi il valore x0 a cui far tendere la x nell'apposita casella di testo.

Successivamente premere il pulsante "Calculate and generate the graph" per ottenere il risultato finale e il grafico.

Se si vuole visualizzare in maniera più accurata il grafico sarà sufficiente premere sul pulsante che compare dopo aver premuto su "Calculate and generate the graph", ovvero "View the detailed graph".

Funzionalità dalla versione "1.4" è la modalità "Live calculation": se è spuntata permette di calcolare e generare automaticamente il grafico in tempo reale, quindi mentre si scrive.

--- VERSIONE SYMPY ---
La versione Sympy ha le medesime funzionalità della versione normale, eccetto che utilizza la libreria "Sympy" piuttosto che il calcolo "meccanico".
Non esiste una casella di testo per numeratore e per denominatore perchè, di fatto, è più "intelligente".
Se si vuole inserire un numeratore e un denominatore sarà sufficiente scrivere ciò che si vuole al numeratore "/" ciò che si vuole al denominatore. Un esempio:
Numeratore: x+2 || Denominatore: x^3+5
-> (x+2)/(x\*\*3+5)
è possibile notare anche che si può andare oltre al grado secondo, arrivando a quello che si preferisce e che, per fare l'elevazione è necessario mettere 2 "\*" di seguito.

Per il simbolo di infinito vengono usate due "o" vicine: oo (_il sistema non riconosce ancora e non sostituisce in automatico se viene inserito il simbolo ∞ o "inf"_).

- infinito -> oo
- elevazione -> **

## Screenshots
Sono presenti alcuni screenshot del software nella cartella "screenshot"

## Librerie utilizzate
- PyQt5
- Matplotlib
- Sympy (per versione "sympy")

## Come collaborare
Collaborare al progetto è molto semplice: è sufficiente aprire un nuovo issue in caso si vogliano aggiungere nuove funzionalità, successivamente si può procedere alla pr (su indicazione di un moderatore).
Si può collaborare anche solo segnalando un problema o dando un consiglio.


**NB. Viene effettuato il merge delle pr direttamente (e solamente) da Sav22999.**

## OS su cui è testato il software
Sono stati effettuati differenti test sui seguenti sistemi operativi, sui quali è garantita la compatibilità:
- Kubuntu (18.04)
- Ubuntu (18.04)
- Windows 10 (Home)

## Collaboratori
- Sav22999 - Saverio Morelli - https://www.saveriomorelli.com/
- Mone27 - Simone Massaro
