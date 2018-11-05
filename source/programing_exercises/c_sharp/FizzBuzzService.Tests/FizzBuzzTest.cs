using System;
using Xunit;

namespace FizzBuzzService.Tests
{
    public class FizzBuzzTest
    {
        [Fact]
        public void 値が３ならばFizzを返す()
        {
            Assert.Equal("3", "Fizz");
        }
    }
}
