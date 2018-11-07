using System;
using System.Collections.Generic;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzzTest : IDisposable
    {
        FizzBuzz _fizzBuzz;
        Type _typeStandard;
        public FizzBuzzTest()
        {     
            _fizzBuzz = new FizzBuzz();
            _typeStandard = new TypeStandard();
        }
        public void Dispose(){}        

        [Fact]
        public void 値が３ならばFizzを返す()
        {                                    
            Type actual = _typeStandard;
            actual.generate(3);            
            Assert.Equal("Fizz", actual.Value);
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            Type actual = _typeStandard;
            actual.generate(5);
            Assert.Equal("Buzz", actual.Value);
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            Type actual = _typeStandard;
            actual.generate(15);
            Assert.Equal("FizzBuzz", actual.Value);
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
            Type fizzBuzz = new Type01();
            fizzBuzz.generate(3);            
            Assert.Equal("3", fizzBuzz.Value);
        }
        [Fact]
        public void タイプ２はFizzだけを返す()
        {
            Type fizzBuzz = new Type02();
            fizzBuzz.generate(5);
            Assert.Equal("Fizz", fizzBuzz.Value);
        }     
        [Fact]   
        public void タイプ３はBuzzだけを返す()
        {            
            Type fizzBuzz = new Type03();
            fizzBuzz.generate(3);
            Assert.Equal("Buzz", fizzBuzz.Value);
        }   
        [Fact]
        public void タイプ４は通常パターンを大文字に変換して返す()
        {
            Type fizzBuzz = new Type04();
            fizzBuzz.generate(3);
            Assert.Equal("FIZZ", fizzBuzz.Value);
            fizzBuzz.generate(5);
            Assert.Equal("BUZZ", fizzBuzz.Value);            
            fizzBuzz.generate(15);
            Assert.Equal("FIZZBUZZ", fizzBuzz.Value);            
        }   
        [Fact]
        public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す()
        {
            Type fizzBuzz = new Type05();
            fizzBuzz.generate(2);
            Assert.Equal("Fizz", fizzBuzz.Value);
            fizzBuzz.generate(3);
            Assert.Equal("Buzz", fizzBuzz.Value);            
            fizzBuzz.generate(6);
            Assert.Equal("FIZZBUZZ", fizzBuzz.Value);            
        }                  
    }
}
