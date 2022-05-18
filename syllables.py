"""stuff to devide a sentence in syllables

Usage.

Division:
    syllables = syllables(sentence,lang)
    where sentence is the sentence you want to devide and lang is the lagnuage
    in witch the sentence is forumlated.

This returns an instance of a class with the following public methods:
    one() --> returns the letters in the sentence if there are more consecutive "punteggiatura" will use only one
    ita() --> returns the division in the italian language
    jpn() --> returns the division in the jpanaes language (the frase neads to be in romanji)
    ita() --> returns the division in the english language

fetching aviable languages:
    AviableLanguages = langs()

"""


vocali = ["a","à","e","è","i","ì","o","ò","u","ù",
          "A","À","E","È","I","Ì","O","Ò","U","Ù"]
punteggiatura = [" " , "," , "." , "?" , "!" , ":" , ";"]

lang = ["one","ita","jpn","eng"]
__all__ = ["Error","syllables","langs"]

class Error(Exception):
    pass

def langs():
    return lang

class syllables:
    def __init__(self, sentence, lang = "one") -> None:
        self.F = sentence
        if lang == "one":
            self.one()
        elif lang == "ita":
            self.ita()
        elif lang == "jpn":
            self.jpn()
        elif lang == "eng":
            self.eng()
        else:
            raise Error("LANGUAGE::NOT::FOUND")

    def one(self):
        lettere = []
        pausa = False
        for lettera in self.F:
            if lettera in punteggiatura:
                if pausa:
                    continue
                else:
                    pausa = True
                    lettere.append(" ")
                    continue

            lettere.append(lettera)
            pausa = False
    
        self.S = lettere
        return lettere

    def ita(self):
        #divide la frase in parole
        parole = []
        parola = ""
        prev = False
        for let in self.F:
            if let == " " or let == "," or let == "." or let == "?" or let == "!" or let == ":" or let == ";":
                if prev:
                    parole.append(parola)
                    prev = False
                parole.append(let)
                parola = ""
            else:
                prev = True
                parola += let
        parole.append(parola)
        del parola

        #procedo alla divisione
        #ad ogni vocale divido
        primaDivisione = []
        for parola in parole:
            if len(parola) == 0:
                continue

            i = 0
            parolaPrimaDivisione = parola
            while i != len(parolaPrimaDivisione) - 1:
                carp = parolaPrimaDivisione[i]
                if carp in vocali:
                    i += 1
                    parolaPrimaDivisione = parolaPrimaDivisione[:i] + "-" + parolaPrimaDivisione[i:]
                    
                i += 1
            primaDivisione.append(parolaPrimaDivisione)
            del parola

        #ad ogni doppia divido
        secondaDivisione = []
        for parola in primaDivisione:
            i = 0
            parolaSecondaDivisione = parola
            while i != len(parolaSecondaDivisione) - 1:
                car = parolaSecondaDivisione[i]
                prosCar = parolaSecondaDivisione[i + 1]
                if car == prosCar:
                    i += 1
                    parolaSecondaDivisione = parolaSecondaDivisione[:i] + "-" + parolaSecondaDivisione[i:]
                    
                i += 1
            secondaDivisione.append(parolaSecondaDivisione)
            del parola

        #procedo alla riunione delle sillabe
        #controllo qu + vocale
        primaRiunione = []
        for parola in secondaDivisione:
            if len(parola) <= 4:
                primaRiunione.append(parola)
                continue

            i = 3
            parolaPrimaRiunione = parola
            while i != len(parolaPrimaRiunione):
                car = parolaPrimaRiunione[i]
                PrevistoCutCar = parolaPrimaRiunione[i - 1]
                prevCar = parolaPrimaRiunione[i - 2]
                prevprevCar = parolaPrimaRiunione[i - 3]
                if prevprevCar == "q" and (prevCar == "u" or prevCar == "ù") and PrevistoCutCar == "-" and ((car == "a" or car == "à") or (car == "e" or car == "è") or (car == "i" or car == "ì") or (car == "o" or car == "ò")):
                    parolaPrimaRiunione = (parolaPrimaRiunione[:(i)].removesuffix("-")) + parolaPrimaRiunione[(i):]
                i += 1

            primaRiunione.append(parolaPrimaRiunione)
            del parola

        #controllo doppie
        secondaRiunione = []
        for parola in primaRiunione:
            if len(parola) <= 2:
                secondaRiunione.append(parola)
                continue
            i = 0
            parolaSecondaRiunione = parola
            while i != len(parolaSecondaRiunione)-2:
                car = parolaSecondaRiunione[i]
                PrevistoCutCar = parolaSecondaRiunione[i +1]
                prosCar = parolaSecondaRiunione[i + 2]
                if PrevistoCutCar == "-" and car == prosCar:
                    parolaSecondaRiunione = (parolaSecondaRiunione[:(i)].removesuffix("-")) + parolaSecondaRiunione[(i):]
                    i += 1
                    continue
                i += 1

            secondaRiunione.append(parolaSecondaRiunione)
            del parola

        #vocali spaiate
        terzaRiunione = []
        for parola in secondaRiunione:
            if len(parola) <= 2:
                terzaRiunione.append(parola)
                continue
            i = 0
            parolaTerzaRiunione = parola
            while i != len(parolaTerzaRiunione)-1:
                carp = parolaTerzaRiunione[i]
                PrevistoCutCar = parolaTerzaRiunione[i + 1]

                if (PrevistoCutCar == "-") and  carp in vocali:
                    parolaTerzaRiunione = (parolaTerzaRiunione[:(i)].removesuffix("-")) + parolaTerzaRiunione[(i):]
                    i += 1
                    continue
                i += 1

            terzaRiunione.append(parolaTerzaRiunione)
            del parola
        
        #sistemazione delle parole corte 
        quartaRiunione = []
        for parola in terzaRiunione:
            if len(parola) == 3:
                if parola[1] == "-":
                    newParola = parola[:1] + parola[2:]
                    quartaRiunione.append(newParola)
            else:
                quartaRiunione.append(parola)
            del parola

        #stacco le n-m
        quintaRiunione = []
        for parola in quartaRiunione:
            i = 0
            parolaQuintaRiunione = ""
            while i < len(parola):
                car = parola[i]
                if car == "-":
                    if parola[i+1] in ["n","m"]:
                        parolaQuintaRiunione += parola[i+1] + "-"
                        i += 1
                    else:
                        parolaQuintaRiunione += "-"
                else:
                    parolaQuintaRiunione += car
                
                i += 1
            
            quintaRiunione.append(parolaQuintaRiunione)

        #metto la frase in un array
        sillabeArray = []
        for parola in quintaRiunione:
            parolaArray = []
            sillaba = ""
            for car in parola:
                if car == "-":
                    parolaArray.append(sillaba)
                    sillaba = ""
                else:
                    sillaba += car
            parolaArray.append(sillaba)


            sillabeArray.append(parolaArray)
    
        self.S = sillabeArray
        return sillabeArray

    def jpn(self):
        sillabe = []
        sillaba = ""

        for car in self.F:
            sillaba += car
            if car in vocali:
                sillabe.append(sillaba)
                sillaba = ""

        primaRiunione =[]
        sillabaPrimaDivisione = ""
        for sillaba in sillabe:
            if len(sillaba) == 1:
                primaRiunione.append(sillaba)
                continue
            
            for i in range(len(sillaba) - 2):
                if sillaba[i] == sillaba[i+1]:
                    sillabaPrimaDivisione += sillaba[i]
                    primaRiunione.append(sillabaPrimaDivisione)
                    sillabaPrimaDivisione = "" 
                else:
                    sillabaPrimaDivisione += sillaba[i]
            
            sillabaPrimaDivisione += sillaba[len(sillaba)-2] + sillaba[len(sillaba)-1]
            
            primaRiunione.append(sillabaPrimaDivisione)
            sillabaPrimaDivisione = "" 
        
        self.S = primaRiunione
        return primaRiunione

    def eng(self):

        #divide la frase in parole
        parole = []
        parola = ""
        prev = False
        for let in self.F:
            if let == " " or let == "," or let == "." or let == "?" or let == "!" or let == ":" or let == ";":
                if prev:
                    parole.append(parola)
                    prev = False
                parole.append(let)
                parola = ""
            else:
                prev = True
                parola += let

        parole.append(parola)
        del parola

        # VC/CV
        primaDivisione = []
        for parola in parole:
            if len(parola) in [0,1,2]:
                continue
        
            i = 0
            parolaPrimaDivisione = parola
            while i <= len(parolaPrimaDivisione) - 4:
                if (    parolaPrimaDivisione[i]   in vocali and     parolaPrimaDivisione[i+3] in vocali and
                    not parolaPrimaDivisione[i+1] in vocali and not parolaPrimaDivisione[i+2] in vocali ):

                    i += 1
                    parolaPrimaDivisione = parolaPrimaDivisione[:(i+1)] + "-" + parolaPrimaDivisione[(i+1):]
                i += 1
            primaDivisione.append(parolaPrimaDivisione)
            del parola

        # V/CV
        secondaDivisione = []
        for parola in primaDivisione:
            if len(parola) in [0,1]:
                continue

            i = 0
            parolaSecondaDivisione = parola
            while i <= len(parolaSecondaDivisione) - 3:
                if (    parolaSecondaDivisione[i] in vocali and parolaSecondaDivisione[i+2] in vocali and
                    not parolaSecondaDivisione[i+1] in vocali):

                    i += 1
                    parolaSecondaDivisione = parolaSecondaDivisione[:(i)] + "-" + parolaSecondaDivisione[(i):]
                
                i += 1
            
            secondaDivisione.append(parolaSecondaDivisione)
 
        # V/V
        terzaDivisione = []
        for parola in secondaDivisione:
            if len(parola) in [0,1]:
                continue

            i = 0
            parolaTerzaDivisione = parola

            while i <= len(parolaTerzaDivisione) - 3:
                if (parolaTerzaDivisione[i] in vocali and parolaTerzaDivisione[i+1] in vocali):
                    i += 1
                    parolaTerzaDivisione = parolaTerzaDivisione[:(i)] + "-" + parolaTerzaDivisione[(i):]

                i += 1
            
            terzaDivisione.append(parolaTerzaDivisione)

        #metto la frase in un array
        sillabeArray = []
        for parola in terzaDivisione:
            parolaArray = []
            sillaba = ""
            for car in parola:
                if car == "-":
                    parolaArray.append(sillaba)
                    sillaba = ""
                else:
                    sillaba += car
            parolaArray.append(sillaba)


            sillabeArray.append(parolaArray)

        self.S = sillabeArray
        return sillabeArray

if __name__ == "__main__":
    TestOne = syllables(r"Queste sono le lettere dell'alfabeto. Chi canta dalla A alla Z 112!!!","one")
    TestIta = syllables(r"Queste sono le lettere dell'alfabeto. Chi canta dalla A alla Z 112!!!","ita")
    TestJpn = syllables(r"Kora ra wa aru baba be n to no risutodesu. Dare ga A kara Z made issho ni utaimasu ka 110!!!","jpn")
    TestEng = syllables(r"These are the letters of the alphabet. Who sings along from A to Z 911!!!","eng")

    print("TestIta",TestIta.S)
    print("TestJpn",TestJpn.S)
    print("TestEng",TestEng.S)
    print("TestOne",TestOne.S)