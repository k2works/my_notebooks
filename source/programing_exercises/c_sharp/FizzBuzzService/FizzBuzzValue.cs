using System.Collections.Generic;

namespace FizzBuzzService
{
    public class FizzBuzzValue : ValueObject
    {
        public string Value { get; }
        public int Number { get; }

        public FizzBuzzValue(string value, int number)
        {
            Value = value;
            Number = number;
        }

        protected override IEnumerable<object> GetAtomicValues()
        {
            yield return Value;
            yield return Number;
        }
    }
}