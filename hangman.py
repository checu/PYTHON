import xlwt as xlwt
from pip.commands import install

import hangman
import random

#/POCZĄTEK _EXCEL FILE_WORDS
#importowanie slow z excelowego pliku
#import xlrd
#import pandas as pd # biblioteka do excela- bezpetlowe sprawdzanie ilosci pelnych wierszy i kolum

#workbook = xlrd.open_workbook('slowa.xlsx')#otwieranie
#worksheet = workbook.sheet_by_index(0)# wybór arkusza - z nazwy lub indeksem

#df = pd.read_excel('slowa.xlsx', sheetname="Arkusz1") #pobieranie ilości niepustych wierszy w kolumnie- tablica

#cel=eslow=worksheet.cell(random.randint(1,len(df)),0).value # losowanie slowa do zgadniecia
#workbook = xlrd.close_workbook('slowa.xlsx')
#/ KONIEC

#/ POCZĄTEK_NOTATNIK_FILE_WORDS

#file=open("slowa.txt",'r')
#tekst=file.read()
#dooom=tekst.split()
#cel=dooom[random.randint(1,len(dooom)-1)]
#file.close()
#/KONIEC

#/POCZATEK MYSQL_WORDS




#/KONIEC


#strukturalny wisielec

slowa=['mama','kosmita','ziemniaki','marchewka','jajko','gangrena']# przerobić na pobieranie z bazy danych
cel=slowa[random.randint(0,len(slowa)-1)]

#let's play a game

#wyświetlanie ukrytego hasła- wyswietlanie kresek
h='_ '*len(cel)
haslo = list(h)
print(h)
pudlo=0
while pudlo<len(hangman.HANGMAN) | haslo.count("_")!=0: #gramy tak dlugo, az nie wygramy lub przegramy
    #print(haslo)
    guess=input("Podaj literę ") #zawsze pierwsza litera-na wypadek, jak będzie więcej

    #sprawdzamy, czy mamy litere w słowie
    cel.find(guess)#oddaje tylko indeks
    zawiera=cel.count(guess)

#nie ma litery
    if zawiera==0:
        print(hangman.HANGMAN[pudlo])
        pudlo=pudlo+1
        #sprawdz, czy nie ostatni ruch
        if pudlo==len(hangman.HANGMAN):
            print("YOU LOOSE! Szukane słowo to:",cel )
            break

    #elif zawiera==1:
        #haslo[cel.find(guess)*2]=guess

#jest litera
    else:
        indeksy=[poz for poz, char in enumerate(cel) if char == guess]# tablica indeksów, gdzie litera występuje

        for i in range(0,len(indeksy)):

           haslo[indeksy[i]*2]=guess
           haslo=haslo

        print("".join(haslo))

        if haslo.count("_")==0:
            print("WYGRANA")
            break



#obiektowy wisielec
