using System;
using System.Collections.Generic;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzzTest : IDisposable
    {
        FizzBuzzData _data;
        public FizzBuzzTest()
        {
            _data = new FizzBuzzData();
        }
        public void Dispose(){}        

        [Fact]
        public void 値が３ならばFizzを返す()
        {                        
            _data.Value = FizzBuzz.generate(3);
            Assert.Equal(_data.Value, "Fizz");
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            _data.Value = FizzBuzz.generate(5);
            Assert.Equal(_data.Value, "Buzz");
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            _data.Value = FizzBuzz.generate(15);
            Assert.Equal(_data.Value, "FizzBuzz");
        }       
        [Fact]         
        public void 値が１ならば１を返す()
        {
            _data.Value = FizzBuzz.generate(1);
            Assert.Equal(_data.Value, "1");
        }
        [Fact]
        public void 値が１０１ならば１０１を返す()
        {
            _data.Value = FizzBuzz.generate(101);
            Assert.Equal(_data.Value, "101");
        }        
        [Fact]
        public void 回数を５回繰り返し実行したら配列を返す()
        {
            _data.Values = FizzBuzz.iterate(5);
            string[] expect = {"1","2","Fizz","4","Buzz"};
            Assert.Equal(_data.Values, expect);
        }
        [Fact]
        public void 回数を１０回繰り返し実行したら配列を返す()
        {
            _data.Values = FizzBuzz.iterate(10);
            string[] expect = {"1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"};
            Assert.Equal(_data.Values, expect);
        }
        [Fact]
        public void タイプ１は値を返す()
        {
            _data.Value = FizzBuzz.generate(3, 1);
            Assert.Equal(_data.Value, "3");
        }
        [Fact]
        public void タイプ２はFizzだけを返す()
        {
            _data.Value = FizzBuzz.generate(5, 2);
            Assert.Equal(_data.Value, "Fizz");
        }     
        [Fact]   
        public void タイプ３はBuzzだけを返す()
        {
            _data.Value = FizzBuzz.generate(3, 3);
            Assert.Equal(_data.Value, "Buzz");
        }   
        [Fact]
        public void タイプ４は通常パターンを大文字に変換して返す()
        {
            _data.Value = FizzBuzz.generate(3, 4);
            Assert.Equal(_data.Value, "FIZZ");
            _data.Value = FizzBuzz.generate(5, 4);
            Assert.Equal(_data.Value, "BUZZ");            
            _data.Value = FizzBuzz.generate(15, 4);
            Assert.Equal(_data.Value, "FIZZBUZZ");            
        }   
        [Fact]
        public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す()
        {
            _data.Value = FizzBuzz.generate(2, 5);
            Assert.Equal(_data.Value, "Fizz");
            _data.Value = FizzBuzz.generate(3, 5);
            Assert.Equal(_data.Value, "Buzz");            
            _data.Value = FizzBuzz.generate(6, 5);
            Assert.Equal(_data.Value, "FIZZBUZZ");            
        }                  
    }
}
