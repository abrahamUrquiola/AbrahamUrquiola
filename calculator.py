class MyArray:
    def __init__(self, mayor, menor, promedio):
        self.mayor = mayor
        self.menor = menor
        self.promedio = promedio


class Calculator:
    def add(self, val1, val2):
        return val1+ val2

    def valid_age(self, value):
        return 0 < value < 100

    def max(self, val1, val2, val3):
        if val1 > val2 and val1 > val3:
            return val1
        else:
            if val2 > val3:
                return val2
            else:
                return val3

    def isVocal(self, value):
        if value == 'a' or value == 'e' or value == 'i' or value == 'o' or value == 'u':
            return 'is vocal'
        else:
            if value == 0 or value == 1 or value == 2 or value == 3 or value == 4 or value == 5 or value == 6 or value == 7 or value == 8 or value == 9:
                return 'is number'
            else:
                return 'is consonant'

    def inversa(self, value):
        str = ""
        for i in value:
            str = i + str
        return str

    def palindromo(self, value):
        str = ""
        for i in value:
            str = i + str
        if value == str:
            return True
        else:
            return False



    def mayMenProm(self, array):
        may = 0
        men = 1000
        prom = 0
        n = 0
        for i in array:
            if array[i] > may:
                may = array[i]
            if array[i] < men:
                men = array[i]
            prom = prom + array[i]
            n = n+1
        prom = prom / n
        a = MyArray(may, men, prom)
        return a.mayor+' '+a.menor+' '+a.promedio

    def convertBinary(self, value):
        binary = format(value, "b")
        return binary

    def totalCaracteres(self, value):
        cantidad = 0
        for i in value:
            cantidad = cantidad +1
        return cantidad

