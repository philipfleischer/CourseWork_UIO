"""
Et objekt av klassen Datasenter skal kunne referere til ett eller
flere objekter av klassen Regneklynge. Et objekt av klassen Regneklynge skal kunne
referere til ett eller flere Rack-objekter, der hvert Rack-objekt igjen refererer til en eller flere
Node-objekter.


"""
from node import Node
from rack import Rack
from regneklynge import Regneklynge
from datasenter import Datasenter
def main():
    node1 = Node(16, 100)
    node1.skrivUt()
    print(node1.antProsessorer())
    print(node1.nokMinne(10))

    rack1 = Rack()
    print(rack1.settInn(node1))
    print(rack1.getAntNoder())
    print(rack1.antProsessorer())
    print(rack1.noderMedNokMinne(8))

    regneklynge1 = Regneklynge(8)
    print(regneklynge1.settInnNode(node1))
    print(regneklynge1.antProsessorer())
    print(regneklynge1.noderMedNokMinne(10))
    print(regneklynge1.antRacks())

    datasenter1 = Datasenter()
    print(datasenter1.lesInnRegneklynge("abel.txt"))
    datasenter1.skrivUtAlleRegneklynger()
    datasenter1.skrivUtRegneklynge(regneklynge1)


main()
