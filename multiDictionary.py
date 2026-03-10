import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dictionaries = {}
        self.dictionaries["Italian"] = d.Dictionary()
        self.dictionaries["English"] = d.Dictionary()
        self.dictionaries["Spanish"] = d.Dictionary()

        self.dictionaries["Italian"].loadDictionary("resources/Italian.txt")
        self.dictionaries["English"].loadDictionary("resources/English.txt")
        self.dictionaries["Spanish"].loadDictionary("resources/Spanish.txt")



    def printDic(self, language):
        if language == "English":
            self.dictionaries["English"].printAll()
        elif language == "Italian":
            self.dictionaries["Italian"].printAll()
        elif language == "Spanish":
            self.dictionaries["Spanish"].printAll()
        else:
            "lingua non disponibile"


    def searchWord(self, words, language):
        if language not in self.dictionaries:
            print("Lingua non disponibile")
            return []

        richwords = []

        diz=self.dictionaries[language]
        for parola in words:
            r = rw.RichWord(parola)
            r.corretta= parola in diz.dict
            richwords.append(r)
        return richwords

