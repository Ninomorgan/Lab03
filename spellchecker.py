import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        frase_pulita = replaceChars(txtIn).lower()
        parole = frase_pulita.split()

        # 2️⃣ inizio timer
        start = time.time()

        # 3️⃣ controllo ortografico usando MultiDictionary
        result = self.multiDict.searchWord(parole, language)

        # 4️⃣ fine timer
        end = time.time()
        elapsed = end - start

        # 5️⃣ parole errate
        errori = [r for r in result if not r.corretta]

        # 6️⃣ stampa risultati
        print("\nParole errate:")
        for r in errori:
            print(r)

        print(f"Numero di errori: {len(errori)}")
        print(f"Tempo impiegato: {elapsed:.5f} secondi\n")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~?!"
    for c in chars:
        text = text.replace(c, "")
    return text