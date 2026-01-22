"""
Oppgavebeskrivelse:
Klassen Datasenter skal ta vare på en ordbok med regneklynger. Klassen skal også kunne
lese inn regneklynger fra fil. For å få til dette trenger Datasenter en metode som tar imot et
filnavn og oppretter en regneklynge basert på informasjonen i filen. Filnavnet vil bestå av
regneklyngens navn og filendelsen .txt. Du kan bruke regneklyngens navn som nøkkel i
ordboken og du kan anta at ingen regneklynger heter det samme.
Filen det skal leses inn fra har følgende format:
# Max noder per rack
# AntallNoder MinnePerNode AntallProsessorerPerNode
# AntallNoder MinnePerNode AntallProsessorerPerNode
# …
Klassen Datasenter trenger også en metode for å skrive ut informasjon om én spesifikk
regneklynge og en metode for å skrive ut informasjon om alle regneklyngene i datasenteret.
"""

from regneklynge import Regneklynge
## Klasse for representasjon av et datasenter
#
class Datasenter:

	## Oppretter et datasenter
	#
	def __init__(self):
		self._ordbok = {}

	## Leser inn data om en regneklynge fra fil og legger
	# den til i ordboken
	# @param filnavn filene der dataene for regneklyngen ligger
	"""
	filnavn.readline()
	if filnavn[0] != True:
		linje.strip().split()
		Fortsette med resten av kommandoene.
	"""
	def lesInnRegneklynge(self, filnavn):
		lestFil = open(filnavn, "r")
		linje = lestFil.strip().split()
		for linje in lestFil:
			maksNoder = linje[0]
			print(linje[0])
			antNoder = linje[1][0]
			print(antNoder)
			self._ordbok[maksNoder] = antNoder
			return maksNoder, antNoder

	## Skriver ut informasjon om alle regneklyngene
	#
	def skrivUtAlleRegneklynger(self):
		for i in regneklynge:
			print(i)

	## Skriver ut informasjon om en spesifikk regeklynge
	# @param navn navnet på regnekyngen
	def skrivUtRegneklynge(self, navn):
		for navn in regneklynge:
			if navn == regneklynge:
				print(navn)


#Lag et testprogram under
"""
def main():
    datasenter1 = Datasenter()
    print(datasenter1.lesInnRegneklynge("saga.txt"))

main()
"""
