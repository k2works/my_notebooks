using System.Collections.Generic;
using System.Linq;
using FizzBuzzService.Type;
using FizzBuzzService.Value;

namespace FizzBuzzService.Command
{
    public class FizzBuzzValuesCommand : ICommand
    {
        private readonly FizzBuzzType _type;
        private FizzBuzzValues _values;

        public FizzBuzzValuesCommand(FizzBuzzType type)
        {
            _type = type;
            var list = new List<FizzBuzzValue>();
            _values = new FizzBuzzValues(list);
        }

        public void Execute(int count)
        {
            foreach (var i in Enumerable.Range(1, count))
            {
                var fizzBuzzValue = _type.Generate(i);
                _values = _values.Add(fizzBuzzValue);
            }
        }

        public string[] GetResult()
        {
            return _values.ArrayValue();
        }
    }
}