using FizzBuzzService.Value;

namespace FizzBuzzService.Type
{
    public abstract partial class FizzBuzzType
    {
        private class Type04 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int number)
            {
                var value = base.Generate(number);

                return new FizzBuzzValue(value.Value.ToUpper(), number);
            }
        }
    }
}