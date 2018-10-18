# frozen_string_literal: true

class FizzBuzz
  def self.generate(number)
    value = number

    if (value % 3 == 0) && (value % 5 == 0)
      value = 'FizzBuzz'
    elsif value % 3 == 0
      value = 'Fizz'
    elsif value % 5 == 0
      value = 'Buzz'
    end

    value
  end

  def self.iterate(count)
    array = []
    count.times do |n|
      n += 1
      array.push(FizzBuzz.generate(n))
    end
    array
  end
end

require 'minitest/autorun'
class FizzBuzzSpec < Minitest::Spec
  describe FizzBuzz do
    it '3ならばFizzを返す' do
      expect(FizzBuzz.generate(3)).must_equal 'Fizz'
    end

    it '9ならばFizzを返す' do
      expect(FizzBuzz.generate(9)).must_equal 'Fizz'
    end

    it '5ならばBuzzを返す' do
      expect(FizzBuzz.generate(5)).must_equal 'Buzz'
    end

    it '10ならばBuzzを返す' do
      expect(FizzBuzz.generate(10)).must_equal 'Buzz'
    end

    it '50ならばBuzzを返す' do
      expect(FizzBuzz.generate(50)).must_equal 'Buzz'
    end

    it '15ならばFizzBuzzを返す' do
      expect(FizzBuzz.generate(15)).must_equal 'FizzBuzz'
    end

    it '30ならばFizzBuzzを返す' do
      expect(FizzBuzz.generate(30)).must_equal 'FizzBuzz'
    end

    it '5回実行されたならば配列を返す' do
      expect(FizzBuzz.iterate(5)).must_equal [1, 2, 'Fizz', 4, 'Buzz']
    end

    it '10回実行されたならば配列を返す' do
      expect(FizzBuzz.iterate(10)).must_equal [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
    end
  end
end
