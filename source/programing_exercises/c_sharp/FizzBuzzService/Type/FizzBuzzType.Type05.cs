using FizzBuzzService.Value;

namespace FizzBuzzService.Type
{
    public abstract partial class FizzBuzzType
    {
        private class Type05 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int v)
            {
                var number = new Number(v);
                return number.CanDivideTwoAndThree() ? new FizzBuzzValue("FIZZBUZZ", number.Value) :
                    number.CanDivideTwo() ? new FizzBuzzValue("Fizz", number.Value) :
                    number.CanDivideThree() ? new FizzBuzzValue("Buzz", number.Value) :
                    new FizzBuzzValue(number.ToString(), number.Value);
            }
        }
    }
}