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