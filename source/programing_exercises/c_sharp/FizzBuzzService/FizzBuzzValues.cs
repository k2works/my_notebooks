using System.Collections.Generic;

namespace FizzBuzzService
{
    public class FizzBuzzValues
    {
        private readonly List<FizzBuzzValue> _fizzBuzzValueCollection;

        public FizzBuzzValues(List<FizzBuzzValue> fizzBuzzValueCollection) =>
            _fizzBuzzValueCollection = fizzBuzzValueCollection;

        public FizzBuzzValues Add(FizzBuzzValue fizzBuzzValue)
        {
            var result = new List<FizzBuzzValue>(_fizzBuzzValueCollection) {fizzBuzzValue};
            return new FizzBuzzValues(result);
        }

        public string[] ArrayValue()
        {
            var result = new string[_fizzBuzzValueCollection.Count];
            var i = 0;
            foreach (var each in _fizzBuzzValueCollection)
            {
                result[i] = each.Value;
                i = i + 1;
            }

            return result;
        }
    }
}