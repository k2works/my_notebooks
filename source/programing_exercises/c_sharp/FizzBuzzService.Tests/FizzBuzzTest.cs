using System;
using System.Collections.Generic;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzzTest : IDisposable
    {
        FizzBuzz _fizzBuzz;
        public FizzBuzzTest()
        {     
            _fizzBuzz = new FizzBuzz();
        }
        public void Dispose(){}        

        [Fact]
        public void 値が３ならばFizzを返す()
        {                        
            _fizzBuzz.generate(3);            
            Assert.Equal("Fizz", _fizzBuzz.Value);
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            _fizzBuzz.generate(5);
            Assert.Equal("Buzz", _fizzBuzz.Value);
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            _fizzBuzz.generate(15);
            Assert.Equal("FizzBuzz", _fizzBuzz.Value);
        }       
        [Fact]         
        public void 値が１ならば１を返す()
        {
            _fizzBuzz.generate(1);
            Assert.Equal("1", _fizzBuzz.Value);
        }
        [Fact]
        public void 値が１０１ならば１０１を返す()
        {
            _fizzBuzz.generate(101);
            Assert.Equal("101", _fizzBuzz.Value);
        }        
        [Fact]
        public void 回数を５回繰り返し実行したら配列を返す()
        {
            _fizzBuzz.iterate(5);
            string[] expect = {"1","2","Fizz","4","Buzz"};
            Assert.Equal(expect, _fizzBuzz.Values);
        }
        [Fact]
        public void 回数を１０回繰り返し実行したら配列を返す()
        {
            _fizzBuzz.iterate(10);
            string[] expect = {"1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"};
            Assert.Equal(expect, _fizzBuzz.Values);
        }
        [Fact]
        public void タイプ１は値を返す()
        {
            _fizzBuzz.generate(3, 1);
            Assert.Equal("3", _fizzBuzz.Value);
        }
        [Fact]
        public void タイプ２はFizzだけを返す()
        {
            _fizzBuzz.generate(5, 2);
            Assert.Equal("Fizz", _fizzBuzz.Value);
        }     
        [Fact]   
        public void タイプ３はBuzzだけを返す()
        {
            _fizzBuzz.generate(3, 3);
            Assert.Equal("Buzz", _fizzBuzz.Value);
        }   
        [Fact]
        public void タイプ４は通常パターンを大文字に変換して返す()
        {
            _fizzBuzz.generate(3, 4);
            Assert.Equal("FIZZ", _fizzBuzz.Value);
            _fizzBuzz.generate(5, 4);
            Assert.Equal("BUZZ", _fizzBuzz.Value);            
            _fizzBuzz.generate(15, 4);
            Assert.Equal("FIZZBUZZ", _fizzBuzz.Value);            
        }   
        [Fact]
        public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す()
        {
            _fizzBuzz.generate(2, 5);
            Assert.Equal("Fizz", _fizzBuzz.Value);
            _fizzBuzz.generate(3, 5);
            Assert.Equal("Buzz", _fizzBuzz.Value);            
            _fizzBuzz.generate(6, 5);
            Assert.Equal("FIZZBUZZ", _fizzBuzz.Value);            
        }                  
    }
}
