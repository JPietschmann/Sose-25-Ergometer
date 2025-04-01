class Sensor():
    """
    A sensor class that represents a sensor
    """
    #Konstruktor
    def init(self, id):
        self.id = id
        self.messwert = None
        self.messwerte = []
        self.passwort = "123456" #tut dann so als gäbe es das Attribut nicht, ausgabe wie unten (im dictl. kommt es trotzdem)

    def measure(self, messwert): 
        self.messwert = messwert
        self.messwerte.append(messwert)

    def calc_mean(self):
        self.mittelwert = sum(self.messwerte)/len(self.messwerte)
        return self.mittelwert #direkt zurückgeben

    def get_passwort(self, superpasswort):
        if superpasswort =="bier":
            return self.passwort 

    def set_passwort(self, superpasswort, neues_passwort):
        if superpasswort =="bier":
            self.passwort = neues_passwort

    def reset(self, passwort):
        if passwort == self.passwort: 
            print("auf werkseinstellungen")
            self.messwert=None
            self.messwerte=[]
        else:
            print ("Falsches Passwort!") 

if name == "main":
    s1= Sensor("123") #123 ist die id
    print(s1.id)
    s1.measure(10)
    s1.measure(20)
    s1.measure(30)
    print(s1.messwerte)
    s1.calc_mean()
    print(s1.calc_mean())
    das_passwort=s1.get_passwort("bier")
    print(das_passwort)
    print(s1.dict) #ein Dictionary mit allen Attributen (nicht Methoden) von Objekten, automatisch bei Klassen
    s1.reset(das_passwort)