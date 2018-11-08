using FizzBuzzService.Type;
using FizzBuzzService.Value;

namespace FizzBuzzService.Command
{
    public class FizzBuzzValueCommand : ICommand
    {
        private readonly FizzBuzzType _type;
        private FizzBuzzValue _value;

        public FizzBuzzValueCommand(FizzBuzzType type)
        {
            _type = type;
        }

        public void Execute(int number)
        {
            _value = _type.Generate(number);
        }

        public FizzBuzzValue GetResult()
        {
            return _value;
        }
    }
}