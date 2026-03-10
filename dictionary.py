class Dictionary:
    def __init__(self):
        self._dict = set()  #creo un set privato _


    def loadDictionary(self,path):
        with open(path,'r', encoding='utf-8') as f:   #leggo un file
            for line in f:
                parola=line.lower().strip() #per ongi linea caccio spazi e la rendo minuscola
                if parola not in self.dict: #se la parola non c'è la aggiungo
                    self.dict.add(parola)


    def printAll(self):
        print(self.dict)


    @property
    def dict(self): #SAREBBE IL MIO GET
        return self._dict

if __name__ == "__main__":
    d= Dictionary()
    d.loadDictionary("resources/Italian.txt")
    d.printAll()