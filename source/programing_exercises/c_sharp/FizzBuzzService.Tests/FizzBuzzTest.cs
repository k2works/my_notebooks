using System;
using FizzBuzzService.Command;
using FizzBuzzService.Type;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzzTest : IDisposable
    {
        readonly FizzBuzzType _typeOne;
        readonly FizzBuzzType _typeTwo;
        readonly FizzBuzzType _typeThree;
        readonly FizzBuzzType _typeFour;
        readonly FizzBuzzType _typeFive;
        readonly FizzBuzzType _typeStandard;
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
            var command = new FizzBuzzValueCommand(_typeStandard);
            command.Execute(3);
            var actual = command.GetResult();
            Assert.Equal("Fizz", actual.Value);            
            Assert.Equal(3, actual.Number);
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            var command = new FizzBuzzValueCommand(_typeStandard);
            command.Execute(5);
            var actual = command.GetResult();
            Assert.Equal("Buzz", actual.Value);
            Assert.Equal(5, actual.Number);
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            var command = new FizzBuzzValueCommand(_typeStandard);
            command.Execute(15);
            var actual = command.GetResult();
            Assert.Equal("FizzBuzz", actual.Value);
            Assert.Equal(15, actual.Number);
        }       
        [Fact]         
        public void 値が１ならば１を返す()
        {
            var command = new FizzBuzzValueCommand(_typeStandard);
            command.Execute(1);            
            var actual = command.GetResult();
            Assert.Equal("1", actual.Value);
            Assert.Equal(1, actual.Number);
        }
        [Fact]
        public void 値が１０１ならば１０１を返す()
        {
            var command = new FizzBuzzValueCommand(_typeStandard);
            command.Execute(101);            
            var actual = command.GetResult();
            Assert.Equal("101", actual.Value);
            Assert.Equal(101, actual.Number);            
        }        
        [Fact]
        public void 回数を５回繰り返し実行したら配列を返す()
        {
            var command = new FizzBuzzValuesCommand(_typeStandard);
            command.Execute(5);
            var actual = command.GetResult();
            string[] expect = {"1","2","Fizz","4","Buzz"};
            Assert.Equal(expect, actual);
        }
        [Fact]
        public void 回数を１０回繰り返し実行したら配列を返す()
        {
            var command = new FizzBuzzValuesCommand(_typeStandard);
            command.Execute(10);
            var actual = command.GetResult();            
            string[] expect = {"1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"};
            Assert.Equal(expect, actual);
        }
        [Fact]
        public void タイプ１を５回繰り返し実行したら配列を返す()
        {
            var command = new FizzBuzzValuesCommand(_typeOne);
            command.Execute(5);
            var actual = command.GetResult();                        
            string[] expect = {"1","2","3","4","5"};
            Assert.Equal(expect, actual);
        }
        [Fact]
        public void タイプ１は値を返す()
        {
            var command = new FizzBuzzValueCommand(_typeOne);
            command.Execute(3);            
            var actual = command.GetResult();
            Assert.Equal("3", actual.Value);
        }
        [Fact]
        public void タイプ２はFizzだけを返す()
        {
            var command = new FizzBuzzValueCommand(_typeTwo);
            command.Execute(5);            
            var actual = command.GetResult();
            Assert.Equal("Fizz", actual.Value);
        }     
        [Fact]   
        public void タイプ３はBuzzだけを返す()
        {            
            var command = new FizzBuzzValueCommand(_typeThree);
            command.Execute(3);            
            var actual = command.GetResult();
            Assert.Equal("Buzz", actual.Value);
        }   
        [Fact]
        public void タイプ４は通常パターンを大文字に変換して返す()
        {
            var command = new FizzBuzzValueCommand(_typeFour);
            command.Execute(3);            
            var actual = command.GetResult();
            Assert.Equal("FIZZ", actual.Value);
            command.Execute(5);            
            actual = command.GetResult();
            Assert.Equal("BUZZ", actual.Value);            
            command.Execute(15);            
            actual = command.GetResult();
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }   
        [Fact]
        public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す()
        {
            var command = new FizzBuzzValueCommand(_typeFive);
            command.Execute(2);            
            var actual = command.GetResult();
            Assert.Equal("Fizz", actual.Value);
            command.Execute(3);            
            actual = command.GetResult();
            Assert.Equal("Buzz", actual.Value);                        
            command.Execute(6);            
            actual = command.GetResult();
            Assert.Equal("FIZZBUZZ", actual.Value);            
        }                  
    }
}
