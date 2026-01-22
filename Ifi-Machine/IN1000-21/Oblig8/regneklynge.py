"""
Oppgavebeskrivelse:
Klassen Regneklynge skal holde rede på en liste med racks, og må tilby en metode som tar
et nodeobjekt som parameter og plasserer det i et rack med ledig plass. Hvis alle rackene
er fulle, skal det lages et nytt Rack-objekt som legges inn i listen, og noden plasseres i det
nye racket.
Tips: Det kan være lurt å ta inn antall noder per rack i konstruktøren til Regneklynge.
"""

from node import Node
from rack import Rack
## Klasse for representasjon av regneklynge i et datasenter.
#
class Regneklynge:
	## Oppretter en regneklynge og setter maks antall
	# det er plass til i et rack
	# @param noderPerRack max antall noder per rack
	def __init__(self, noderPerRack):
		self._noderPerRack = noderPerRack
		self._rackliste = []

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
		for node in self._rackliste:
			if len(self._rackliste) <= noderPerRack:
				node.settInn()

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		antall = 0
		for i in self._rackliste:
			antall += i.antProsessorer()
		return antall

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		antall = 0
		for i in self._rackliste:
			if i.nokMinne(paakrevdMinne) == False:
				antall +=1
		return antall

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		return f'Antall racks i regneklyngen: {len(self._rackliste)}'


#Lag et testprogram under
