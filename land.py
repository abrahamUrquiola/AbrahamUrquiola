from src.transport import Transport


class Land(Transport):
    def __init__(self, name, price, hasMotor):
        super().__init__(name, price)
        self.hasMotor = hasMotor

    def displayData(self):
        print('name: '+ self.get_name())
        print('price: ', self.get_price())
        if self.hasMotor:
            print('hasMotor: Yes')
        else:
            print('hasMotor: No')

    def get_hasMotor(self):
        return self.hasMotor
