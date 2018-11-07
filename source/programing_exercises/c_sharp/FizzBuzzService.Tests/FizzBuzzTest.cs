using System;
using System.Collections.Generic;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzzTest : IDisposable
    {
        FizzBuzz _fizzBuzz;
        FizzBuzzType _typeOne;
        FizzBuzzType _typeTwo;
        FizzBuzzType _typeThree;
        FizzBuzzType _typeFour;
        FizzBuzzType _typeFive;
        FizzBuzzType _typeStandard;
        public FizzBuzzTest()
        {     
            _fizzBuzz = new FizzBuzz();
            _typeOne = FizzBuzzType.One;
            _typeTwo = FizzBuzzType.Two;
            _typeThree = FizzBuzzType.Three;
            _typeFour = FizzBuzzType.Four;
            _typeFive = FizzBuzzType.Five;
            _typeStandard = FizzBuzzType.Standard;
        }
        public void Dispose(){}        

        [Fact]
        public void 値が３ならばFizzを返す()
        {                             
            FizzBuzz actual = new FizzBuzz(_typeStandard);
            actual.generate(3);            
            Assert.Equal("Fizz", actual.Value);
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            FizzBuzz actual = new FizzBuzz(_typeStandard);
            actual.generate(5);
            Assert.Equal("Buzz", actual.Value);
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            FizzBuzz actual = new FizzBuzz(_typeStandard);
            actual.generate(15);
            Assert.Equal("FizzBuzz", actual.Value);
        }       
        [Fact]         
        public void 値が１ならば１を返す()
        {
            FizzBuzz actual = new FizzBuzz(_typeStandard);
            actual.generate(1);
            Assert.Equal("1", actual.Value);
        }
        [Fact]
        public void 値が１０１ならば１０１を返す()
        {
            FizzBuzz actual = new FizzBuzz(_typeStandard);
            actual.generate(101);
            Assert.Equal("101", actual.Value);
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
            FizzBuzz actual = new FizzBuzz(_typeOne);
            actual.generate(3);
            Assert.Equal("3", actual.Value);
        }
        [Fact]
        public void タイプ２はFizzだけを返す()
        {
            FizzBuzz actual = new FizzBuzz(_typeTwo);
            actual.generate(5);            
            Assert.Equal("Fizz", actual.Value);
        }     
        [Fact]   
        public void タイプ３はBuzzだけを返す()
        {            
            FizzBuzz actual = new FizzBuzz(_typeThree);
            actual.generate(3);                        
            Assert.Equal("Buzz", actual.Value);
        }   
        [Fact]
        public void タイプ４は通常パターンを大文字に変換して返す()
        {
            FizzBuzz actual = new FizzBuzz(_typeFour);
            actual.generate(3);
            Assert.Equal("FIZZ", actual.Value);
            actual.generate(5);
            Assert.Equal("BUZZ", actual.Value);            
            actual.generate(15);
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }   
        [Fact]
        public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す()
        {
            FizzBuzz actual = new FizzBuzz(_typeFive);
            actual.generate(2);
            Assert.Equal("Fizz", actual.Value);
            actual.generate(3);
            Assert.Equal("Buzz", actual.Value);            
            actual.generate(6);
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }                  
    }
}
