''' Fjerner alle elementene fra en liste'''
def fjern_alt(liste: list):
    while len(liste) > 0:
        liste.pop(0) # fjerner det første elementet i listen

''' Representerer et klassisk kort i kortspill'''
class Spillkort:
    def __init__(self, type: str, verdi: int):
        self.type = type
        self.verdi = verdi
