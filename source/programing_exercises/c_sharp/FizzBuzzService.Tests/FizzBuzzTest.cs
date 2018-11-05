using System;
using System.Collections.Generic;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzz
    {
        internal static String generate(int number)
        {            
            String value = number.ToString();
            
            if (number % 3 == 0 && number % 5 == 0) {
                value = "FizzBuzz";
            } else if (number % 5 == 0) {
                value = "Buzz";
            } else if (number % 3 == 0) {
                value = "Fizz";
            }

            return value;
        }
    }
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
    }
}
