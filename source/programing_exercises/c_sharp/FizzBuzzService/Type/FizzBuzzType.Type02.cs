using FizzBuzzService.Value;

namespace FizzBuzzService.Type
{
    public abstract partial class FizzBuzzType
    {
        private class Type02 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int number) => new FizzBuzzValue("Fizz", number);
        }
    }
}