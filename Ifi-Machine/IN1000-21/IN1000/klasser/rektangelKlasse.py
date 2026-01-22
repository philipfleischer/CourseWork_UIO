class Rektangel:

  def __init__(self, lengde, bredde):
      self._bredde = bredde
      self._lengde = lengde

  def oekLengde(self, oekning):
      self._lengde = oekning

  def oekBredde(self, oekning):
      self._bredde = oekning

  def areal(self):
      return self._lengde * self._bredde

  def omkrets(self):
      return (self._lengde * 4 + self._bredde * 4)

  def reduser(self, redusering):
      return self._lengde - redusering and self._bredde - redusering



rektangel1 = Rektangel(100, 100)
rektangel2 = Rektangel(1,2)

print(rektangel1.areal())
print(rektangel2.areal())

rektangel1.oekLengde(101)
rektangel2.oekBredde(2)

print(rektangel1.omkrets(), rektangel2.omkrets())

print(rektangel1.reduser(10), rektangel2.reduser(15))
