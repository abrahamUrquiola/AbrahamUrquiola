from src import land
from src.land import Land


class ListLandTransport:
    land = list(Land)

    def addLand(self, land):
        l = Land('auto', 1500, True)
        land.append(l)
        l = Land('camion', 17000, True)
        land.append(l)
