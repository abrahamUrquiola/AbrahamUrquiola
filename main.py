from src.transport import Transport
from src.land import Land
from src.car import Car
from src.bicycle import Bicycle
from src.listLandTransport import ListLandTransport

if __name__=="__main__":
    print(10)
    transport1 = Transport('Moto', 2000)
    print(transport1.get_name())
    print(transport1.price)
    transport2 = Land('Foster', 15000, True)
    transport2.displayData()
    transport3 = Bicycle('Santur', 800, False, True)
    transport3.displayData()

