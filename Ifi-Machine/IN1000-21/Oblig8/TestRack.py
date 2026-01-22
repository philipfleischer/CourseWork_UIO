from node import Node
from rack import Rack
def main():
	node1 = Node(16,100)
	node1.skrivUt()
	print(node1.antProsessorer())
	print(node1.nokMinne(15))

	rack1 = Rack()
	print(rack1.settInn(node1))
	print(rack1.getAntNoder())
	print(rack1.antProsessorer())
	print(rack1.noderMedNokMinne(10))
main()
