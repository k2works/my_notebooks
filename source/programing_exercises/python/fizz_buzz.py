class FizzBuzz():
    @staticmethod
    def generate(count):
        value = count

        if value % 3 == 0 and value % 5 == 0:
            value = 'FizzBuzz'
        elif value % 3 == 0:
            value = 'Fizz'
        elif value % 5 == 0:
            value = 'Buzz'

        return value        

    @staticmethod
    def iterate(count):
        array = []

        for n in range(count):
            array.append(FizzBuzz.generate(n + 1))

        return array
