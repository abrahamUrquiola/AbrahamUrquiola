from src.land import Land


class Car(Land):

    def __init__(self, name, price, hasMotor, useGas):
        super().__init__(name, price, hasMotor)
        self.useGas = useGas

    def displayData(self):
        print('name: ' + self.get_name())
        print('price: ', self.get_price())
        if self.get_hasMotor():
            print('hasMotor: Yes')
        else:
            print('hasMotor: No')
        if self.useGas:
            print('useGas: Yes')
        else:
            print('useGas: No')
