"""
Oppgavebeskrivelse:
Klassen Rack skal lagre Node-objektene som hører til et rack i en liste. Vi skal kunne legge
til noder i racket hvis det er færre enn maks antall noder der fra før. For enkelhets skyld skal
vi anta at hvert rack i en regneklynge har plass til like mange noder (men dette maks-tallet
kan variere fra regneklynge til regneklynge). Legg til andre instansvariabler og metoder etter
behov.
"""

## Klasse for representasjon av racks i en regneklynge.
#
class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self):
		self._rack = []

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		self._rack.append(node)
		return self._rack
		"""
		for node in self._rack:
			if node not in self._rack:
				self._rack.append(node)"""


	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		return len(self._rack)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		antall = 0
		for i in self._rack:
			antall += i.antProsessorer()
		return antall

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		for i in self._rack:
			antall = 0
			if i.nokMinne(paakrevdMinne):
				antall += i.nokMinne(paakrevdMinne)
			return antall


#Lag et testprogram under














#s
