const fizzBuzz = require('./fizz_buzz');

describe('TestFizzBuzz', function () {
    it('3ならばFizzを返すようにする', function () {
        expect(fizzBuzz.generate(3)).toBe('Fizz')
    });

    it('5ならばBuzzを返すようにする', function () {
        expect(fizzBuzz.generate(5)).toBe('Buzz')
    });

    it('15ならばFizzBuzzを返すようにする', function () {
        expect(fizzBuzz.generate(15)).toBe('FizzBuzz')
    });

    it('指定された回数だけ実行できるようにする', function () {
        expect(fizzBuzz.iterate(5)).toEqual([1, 2, 'Fizz', 4, 'Buzz'])
    })
});