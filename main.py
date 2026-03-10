import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    print("Inserisci la tua scelta:\n")
    txtIn = input()
    # Add input control here!
    if not txtIn.isdigit():
        print("Scelta non valida!")
        continue

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        frase = input()
        sc.handleSentence(frase,"Italian")

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        frase = input()
        sc.handleSentence(frase,"English")


    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        frase = input()
        sc.handleSentence(frase,"Spanish")

    if int(txtIn) == 4:
        print("fine\n")
        break
    else:
        print("Scelta non valida!")


