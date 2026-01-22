class NorskOrd:
    def __init__(self, ord):
        self._ord = ord

    def sjekkNorske(self):
        tmpOrd = self._ord.lower()
        return ("æ" in tmpOrd or "ø" in tmpOrd or "å" in tmpOrd)

    def fjernNorske(self):
        nyttOrd = ""
        for bokstav in self._ord:
            if bokstav == "æ":
                nyttOrd +="ae"
            elif bokstav == "ø":
                nyttOrd += "oe"
            elif bokstav == "å":
                nyttOrd += "aa"
            elif bokstav == "Æ":
                nyttOrd += "AE"
            elif bokstav == "Ø":
                nyttOrd += "OE"
            elif bokstav == "Å":
                nyttOrd += "AA"
            else:
                nyttOrd += bokstav
        self._ord = nyttOrd

    def skrivOrd(self):
            print ("Ordet er: " + self._ord)

def hovedprogram():
    sesonger = [NorskOrd("Høst"), NorskOrd("høæå")]
    for sesong in sesonger:
        if sesong.sjekkNorske():
            sesong.fjernNorske()

    for sesong in sesonger:
        sesong.skrivOrd()

hovedprogram()
