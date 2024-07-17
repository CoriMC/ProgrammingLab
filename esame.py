class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    
    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        #Preparo la lista per le epoch e le rispettive temperature e la variabile che userò per confrontare le epoch
        lista_dati = []
        epoch_precedente = None
        #Testo se il metodo riesce ad aprire il file
        try:            
            with open(self.name) as file:
                #Dopo aver aperto il file creo una lista composta dalle righe del file
                file_aperto = file.readlines()
        
        except:
            raise ExamException('Errore! Il file non esiste, non funziona oppure il nome presenta errori.')
                
        for elementi in file_aperto:
            #Uso il metodo split() per trasformare ogni riga in una lista
            dati = elementi.split(',')
                    
            if dati[0] != 'epoch':
                #Uso il casting su entrambi gli elementi di ogni lista per convertirli ad int() e float()
                epoch = int(dati[0])
                temperatura = float(dati[1])       
                        
                #Testo che entrambi i campi non siano vuoti
                if epoch == None or temperatura == None:
                    raise ExamException('Errore! Manca uno dei due campi')
                        
                #Controllo che le epoch non siano fuori posto o che non ci siano dei duplicati messi di fila
                if epoch_precedente is not None and epoch <= epoch_precedente:
                    raise ExamException('Errore! Il file presenta un epoch fuori posto oppure duplicato.')
                        
                epoch_precedente = epoch                       
                lista_dati.append([epoch, temperatura])
          
        return lista_dati
        
def compute_daily_max_difference(time_series):
    
    #Creo un dizionario vuoto in cui immagazzinerò day_start_epoch come chiave e come valore avrà la
    #lista di escursioni termiche appartenenti al giorno contrassegnato da uno specifico day_start_epoch
    diz_temperature = {}
    
    #Controllo che l'input sia una lista
    if not isinstance(time_series, list):
        raise Exception('Errore! Devo dare una lista come input perché questo metodo funzioni.')
    
    for lista in time_series:
        epoch = lista[0]
        temperatura = lista[1]
        #Trovo l'inizio della giornata: se sottraggo il modulo di epoch ad epoch otterrò sempre 
        #la mezzanotte del giorno di cui l'orario esaminato fa parte
        day_start_epoch = epoch - (epoch % 86400)
        
        #Se il day_start_epoch non è nel dizionario lo inserisco in esso e come valore gli assegno una lista vuota,
        #in cui inserirò le temperature facenti parte del giorno stesso
        if day_start_epoch not in diz_temperature:
            diz_temperature[day_start_epoch] = []

        diz_temperature[day_start_epoch].append(temperatura)
    
    #Preparo una lista vuota in cui immagazzinerò le differenze
    lista_differenze = []
    
    for day_start_epoch in diz_temperature:        
        lista_temperature = diz_temperature[day_start_epoch]
        
        #Controllo se ci sia una temperatura unica per un giorno, in quel caso inserisco None
        #ma in caso contrario calcolo il minimo ed il massimo e la loro differenza verrà inserita nella lista_differenze
        if len(lista_temperature) <= 1:
            lista_differenze.append(None)
            
        else:
            temperatura_max = max(lista_temperature)
            temperatura_min = min(lista_temperature)
            lista_differenze.append(temperatura_max-temperatura_min)
            
    #Per rendere il programma più specifico per il mese di Marzo si potrebbe anche alzare questa eccezione:         
    #if len(lista_differenze) != 31:
     #   raise ExamException('Errore! La lista non contiene la escursione termica di tutti i giorni del mese di Marzo 2019')

    return lista_differenze