using System;
using System.Collections.Generic;
using Xunit;

namespace FizzBuzzService.Tests
{
        public class FizzBuzzTest
    {
        [Fact]
        public void 値が３ならばFizzを返す()
        {                        
            Assert.Equal(FizzBuzz.generate(3), "Fizz");
        }
        [Fact]
        public void 値が５ならばBuzzを返す()
        {
            Assert.Equal(FizzBuzz.generate(5), "Buzz");
        }
        [Fact]
        public void 値が１５ならばFizzBuzzを返す()
        {
            Assert.Equal(FizzBuzz.generate(15), "FizzBuzz");
        }       
        [Fact]         
        public void 値が１ならば１を返す()
        {
            Assert.Equal(FizzBuzz.generate(1), "1");
        }
        [Fact]
        public void 値が１０１ならば１０１を返す()
        {
            Assert.Equal(FizzBuzz.generate(101), "101");
        }        
        [Fact]
        public void 回数を５回繰り返し実行したら配列を返す()
        {
            string[] expect = {"1","2","Fizz","4","Buzz"};
            Assert.Equal(FizzBuzz.iterate(5), expect);
        }
        [Fact]
        public void 回数を１０回繰り返し実行したら配列を返す()
        {
            string[] expect = {"1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"};
            Assert.Equal(FizzBuzz.iterate(10), expect);
        }        
    }
}
