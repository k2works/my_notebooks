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
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeStandard);
            command.execute(3);
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("Fizz", actual.Value);            
            Assert.Equal(3, actual.Number);
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeStandard);
            command.execute(5);
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("Buzz", actual.Value);
            Assert.Equal(5, actual.Number);
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeStandard);
            command.execute(15);
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("FizzBuzz", actual.Value);
            Assert.Equal(15, actual.Number);
        }       
        [Fact]         
        public void 値が１ならば１を返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeStandard);
            command.execute(1);            
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("1", actual.Value);
            Assert.Equal(1, actual.Number);
        }
        [Fact]
        public void 値が１０１ならば１０１を返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeStandard);
            command.execute(101);            
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("101", actual.Value);
            Assert.Equal(101, actual.Number);            
        }        
        [Fact]
        public void 回数を５回繰り返し実行したら配列を返す()
        {
            FizzBuzzValuesCommand command = new FizzBuzzValuesCommand(_typeStandard);
            command.execute(5);
            string[] actual = command.getResult();
            string[] expect = {"1","2","Fizz","4","Buzz"};
            Assert.Equal(expect, actual);
        }
        [Fact]
        public void 回数を１０回繰り返し実行したら配列を返す()
        {
            FizzBuzzValuesCommand command = new FizzBuzzValuesCommand(_typeStandard);
            command.execute(10);
            string[] actual = command.getResult();            
            string[] expect = {"1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"};
            Assert.Equal(expect, actual);
        }
        [Fact]
        public void タイプ１を５回繰り返し実行したら配列を返す()
        {
            FizzBuzzValuesCommand command = new FizzBuzzValuesCommand(_typeOne);
            command.execute(5);
            string[] actual = command.getResult();                        
            string[] expect = {"1","2","3","4","5"};
            Assert.Equal(expect, actual);
        }
        [Fact]
        public void タイプ１は値を返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeOne);
            command.execute(3);            
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("3", actual.Value);
        }
        [Fact]
        public void タイプ２はFizzだけを返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeTwo);
            command.execute(5);            
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("Fizz", actual.Value);
        }     
        [Fact]   
        public void タイプ３はBuzzだけを返す()
        {            
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeThree);
            command.execute(3);            
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("Buzz", actual.Value);
        }   
        [Fact]
        public void タイプ４は通常パターンを大文字に変換して返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeFour);
            command.execute(3);            
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("FIZZ", actual.Value);
            command.execute(5);            
            actual = command.getResult();
            Assert.Equal("BUZZ", actual.Value);            
            command.execute(15);            
            actual = command.getResult();
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }   
        [Fact]
        public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す()
        {
            FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeFive);
            command.execute(2);            
            FizzBuzzValue actual = command.getResult();
            Assert.Equal("Fizz", actual.Value);
            command.execute(3);            
            actual = command.getResult();
            Assert.Equal("Buzz", actual.Value);                        
            command.execute(6);            
            actual = command.getResult();
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }                  
    }
}
