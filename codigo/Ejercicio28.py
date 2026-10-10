baseWordList =  []
word = ""
while word != "salir":
    print("User, introduce a word")
    word = input()
    baseWordList.append(word)
print(baseWordList)
listaVocales = []
listaConsonantes = []
for birdword in baseWordList:
    print(birdword)
    print(len(birdword))
    if birdword[0].lower() == "a" or birdword[0].lower() == "e" or birdword[0].lower() == "i" or birdword[0].lower() == "o" or birdword[0].lower() == "u":
        listaVocales.append(birdword)
    else:
        listaConsonantes.append(birdword)
vocaTupla = tuple(listaVocales)
constaTupla = tuple(listaConsonantes)
print(vocaTupla)
print(constaTupla)