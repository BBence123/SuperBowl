class Donto:
    def __init__(self, adatsor):
        reszletek = adatsor.split(";")
        #adatmezők kialakítása
        self.ssz = reszletek[0]
        self.datum = reszletek[1]
        self.gyoztes = reszletek[2]
        self.eredmeny = reszletek[3]
        self.vesztes = reszletek[4]
        self.helyszin = reszletek[5]
        self.varosAllam = reszletek[6]
        self.nezoszam = int(reszletek[7])

    def __str__(self):
        return f"{self.datum}, {self.helyszin}: {self.gyoztes} - {self.vesztes} ({self.eredmeny})"
    
    def pontKulonbseg(self):
        reszletek =self.eredmeny.split('-')
        return int(reszletek[0]) - int(reszletek[1]) 

#0
print("SuperBowl döntőinek feldolgozása")

#1
finp = open("SuperBowl.txt", mode="rt", encoding="utf8") 
adatsorok = finp.read().split('\n')
finp.close()

dontok = []
for i in range(1, len(adatsorok)):
    if adatsorok[i] != "":
        dd = Donto(adatsorok[i])
        dontok.append(dd)


#3
for item in dontok:
    print(item)
print("------------------------------------------------------------------------")

#Programozási tételek
#Összegzés tétele
#Határozza meg hogy a SuperBawl döntőket hány ember látogatta meg!

sum = 0
for item in dontok:
    sum += item.nezoszam
print(f"sum = {sum}")

print("------------------------------------------------------------------------")

#átlag
#Határozza meg a látogatól átlagos számát

sum = 0
for item in dontok:
    sum += item.nezoszam
atlag = sum / len(dontok)
print(f"átlag = {atlag:.2f}")

print("------------------------------------------------------------------------")

#min-max tétel
#min
#Határozza meg hogy a döntők között milyen volt a legkisebb pontkülönbség

minPontkulonbseg = dontok[0]
for item in dontok:
    if item.pontKulonbseg() < minPontkulonbseg.pontKulonbseg():
        minPontkulonbseg = item
print(f"min pontkülönbség: {minPontkulonbseg.pontKulonbseg()}")

print("------------------------------------------------------------------------")

#max
#Határozza meg a döntők során elért legnagyobb pontkülönbséget

maxPontkulonbseg = dontok[0]
for item in dontok:
    if item.pontKulonbseg() > maxPontkulonbseg.pontKulonbseg():
        maxPontkulonbseg = item
print(f"max pontkülönbség: {maxPontkulonbseg.pontKulonbseg()}")

print("------------------------------------------------------------------------")

#Határozza meg hogy a döntők során milyen volt a maximális látogatottság

maxNezoszam = dontok[0]
for item in dontok:
    if item.nezoszam > maxNezoszam.nezoszam:
        maxNezoszam = item
print(f"max nézőszám: {maxNezoszam.nezoszam}")

print("------------------------------------------------------------------------")

#megszámlálás tétele
#Határozza meg hogy a döntők során hányszor nyert a Pittsburgh Steelers

dbPS = 0
for item in dontok:
    if item.gyoztes == "Pittsburgh Steelers":
        dbPS += 1
print(f"A 'Pittsburgh Steelers' csapat {dbPS} győzött a döntők során")

print("------------------------------------------------------------------------")

#eldöntés tétele
#legalább egy elem teljesíti a feltételt
#Határozza meg hogy volt-e olyan döntő, ahol a két csapat közötti pontkülönbség meghaladta az 50-et

VanEpontKulonbseg50tobb = False
for item in dontok:
    if item.pontKulonbseg() > 50:
        VanEpontKulonbseg50tobb = True
        break 
if VanEpontKulonbseg50tobb:
    print("Igen volt megfelelő döntő")
else:
    print("Nem volt megfelelő döntő")

print("------------------------------------------------------------------------")

#minden elem teljesíti
#Határozza meg hogy a döntők során minden egyes döntőn a látogatottság meghaladta-e a 70.000-et

mindenEnezoszam70eTobb = True
for item in dontok:
    if not (item.nezoszam > 70000):
        mindenEnezoszam70eTobb = False
        break
if mindenEnezoszam70eTobb:
    print("Minden döntőt teljesíti a feltételt")
else:
    print("Nem minden döntőt teljesíti a feltételt")

print("------------------------------------------------------------------------")

#kiválasztás tétele
#Határozza meg az első olyan döntőt, ahol a nézőszám meghaladta a 100.000

dontoNezoszam100eTobb = None
for item in dontok:
    if item.nezoszam > 10000:
        dontoNezoszam100eTobb = item
        break
if dontoNezoszam100eTobb != None:
    print(f"Van ilyen döntő, amely nézőszáma: {dontoNezoszam100eTobb.nezoszam}")
else:
    print("Nincs megfelelő döntő")

print("------------------------------------------------------------------------")

#Keresés tétele
#Keresse meg az első olyan döntőt, amelyiknél a pontkülönbség a csapatok között 10

indexPontKul0 = None
for i in range(len(dontok)):
    if dontok[i].pontKulonbseg() == 1:
        indexPontKul0 = i
        break
if indexPontKul0 != None:
    print(f"Döntő: {dontok[indexPontKul0]}, NÉSZŐSZÁM: {dontok[indexPontKul0].nezoszam}")
else:
    print("Nincs megfelelő döntő")

print("------------------------------------------------------------------------")

#buborékos rendezés
#Rendezze a döntőket pontkülönbség alapján csökkenő sorrendbe

for i in range(len(dontok)-1, 0, -1):
    for j in range(i):
        if dontok[j].pontKulonbseg() < dontok[j+1].pontKulonbseg():
            dontok[j], dontok[j+1] = dontok[j+1], dontok[j]

for item in dontok:
    print(item)