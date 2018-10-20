module.exports = class FizzBuzz {
    static generate(number) {
        let value = number;

        if (value % 3 === 0 && value % 5 === 0) {
            value = 'FizzBuzz'
        } else if (value % 3 === 0) {
            value = 'Fizz'
        } else if (value % 5 === 0) {
            value = 'Buzz'
        }

        return value;
    }

    static iterate(count) {
    const array = [];

    for (let i = 1; i <= count; i += 1) {
        array.push(FizzBuzz.generate(i));
    }

    return array;
    }
}
