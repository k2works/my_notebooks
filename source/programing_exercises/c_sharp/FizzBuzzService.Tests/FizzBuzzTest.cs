using System;
using System.Collections.Generic;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzzTest : IDisposable
    {
        FizzBuzzType _typeOne;
        FizzBuzzType _typeTwo;
        FizzBuzzType _typeThree;
        FizzBuzzType _typeFour;
        FizzBuzzType _typeFive;
        FizzBuzzType _typeStandard;
        public FizzBuzzTest()
        {     
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
            FizzBuzz fizzBuzz = new FizzBuzz(_typeStandard);
            FizzBuzzValue actual = fizzBuzz.generate(3);            
            Assert.Equal("Fizz", actual.Value);            
            Assert.Equal(3, actual.Number);
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeStandard);
            FizzBuzzValue actual = fizzBuzz.generate(5);            
            Assert.Equal("Buzz", actual.Value);
            Assert.Equal(5, actual.Number);
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeStandard);
            FizzBuzzValue actual = fizzBuzz.generate(15);            
            Assert.Equal("FizzBuzz", actual.Value);
            Assert.Equal(15, actual.Number);
        }       
        [Fact]         
        public void 値が１ならば１を返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeStandard);
            FizzBuzzValue actual = fizzBuzz.generate(1);            
            Assert.Equal("1", actual.Value);
            Assert.Equal(1, actual.Number);
        }
        [Fact]
        public void 値が１０１ならば１０１を返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeStandard);
            FizzBuzzValue actual = fizzBuzz.generate(101);                        
            Assert.Equal("101", actual.Value);
            Assert.Equal(101, actual.Number);            
        }        
        [Fact]
        public void 回数を５回繰り返し実行したら配列を返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeStandard);
            fizzBuzz.iterate(5);
            string[] expect = {"1","2","Fizz","4","Buzz"};
            Assert.Equal(expect, fizzBuzz.Values.arrayValue());
        }
        [Fact]
        public void 回数を１０回繰り返し実行したら配列を返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeStandard);
            fizzBuzz.iterate(10);
            string[] expect = {"1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"};
            Assert.Equal(expect, fizzBuzz.Values.arrayValue());
        }
        [Fact]
        public void タイプ１を５回繰り返し実行したら配列を返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeOne);
            fizzBuzz.iterate(5);
            string[] expect = {"1","2","3","4","5"};
            Assert.Equal(expect, fizzBuzz.Values.arrayValue());
        }
        [Fact]
        public void タイプ１は値を返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeOne);            
            FizzBuzzValue actual = fizzBuzz.generate(3);
            Assert.Equal("3", actual.Value);
        }
        [Fact]
        public void タイプ２はFizzだけを返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeTwo);                        
            FizzBuzzValue actual = fizzBuzz.generate(5);
            Assert.Equal("Fizz", actual.Value);
        }     
        [Fact]   
        public void タイプ３はBuzzだけを返す()
        {            
            FizzBuzz fizzBuzz = new FizzBuzz(_typeThree);                        
            FizzBuzzValue actual = fizzBuzz.generate(3);
            Assert.Equal("Buzz", actual.Value);
        }   
        [Fact]
        public void タイプ４は通常パターンを大文字に変換して返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeFour);                        
            FizzBuzzValue actual = fizzBuzz.generate(3);
            Assert.Equal("FIZZ", actual.Value);
            actual = fizzBuzz.generate(5);
            Assert.Equal("BUZZ", actual.Value);            
            actual = fizzBuzz.generate(15);
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }   
        [Fact]
        public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す()
        {
            FizzBuzz fizzBuzz = new FizzBuzz(_typeFive);                        
            FizzBuzzValue actual = fizzBuzz.generate(2);
            Assert.Equal("Fizz", actual.Value);
            actual = fizzBuzz.generate(3);            
            Assert.Equal("Buzz", actual.Value);                        
            actual = fizzBuzz.generate(6);            
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }                  
    }
}
