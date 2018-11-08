using FizzBuzzService.Value;

namespace FizzBuzzService.Type
{
    public abstract partial class FizzBuzzType
    {
        private class Type01 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int number)
            {
                var value = number.ToString();
                return new FizzBuzzValue(value, number);
            }
        }
    }
}