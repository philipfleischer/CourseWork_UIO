"""
Oppgavebeskrivelse:
Klassen Node skal kunne initiere nye objekter med ønsket minnestørrelse og antall
prosessorer, og for øvrig tilby tjenester (metoder) som trengs i andre deler av programmet.
"""

## Klasse for representasjon av noder i en regneklynge
#
class Node:
	## Oppretter en node med gitt minne-storrelse og antall prosessorer
	#  @param minne GB minne i den nye noden
	#  @param antPros antall prosessorer i den nye noden
	def __init__(self, minne, antPros):
		self._minne = minne
		self._antPros = antPros

	def skrivUt(self):
		print("Node:", self._minne, self._antPros)


	## Henter antall prosessorer i noden
	#  @return antall prosessorer i noden
	def antProsessorer(self):
		return self._antPros

	## Sjekker om noden har tilstrekkelig minne for et program
	#  @param paakrevdMinne GB minne som kreves for programmet
	#  @return True hvis noden har minst så mye minne
	def nokMinne(self, paakrevdMinne):
		if self._minne >= paakrevdMinne:
			return True
		else:
			return False

    #Må lage flere metoder som skal brukes i andre klasser også


    #Lag et testprogram under
