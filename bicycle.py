from src.land import Land


class Bicycle(Land):
    def __init__(self, name, price, hasMotor, exerciseBike):
        super().__init__(name, price, hasMotor)
        self.exerciseBike = exerciseBike

    def displayData(self):
        print('name: ' + self.get_name())
        print('price: ', self.get_price())
        if self.get_hasMotor():
            print('hasMotor: Yes')
        else:
            print('hasMotor: No')
        if self.exerciseBike :
            print('exerciseBike: Yes')
        else:
            print('exerciseBike: No')

