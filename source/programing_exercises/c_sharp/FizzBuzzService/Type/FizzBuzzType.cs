using FizzBuzzService.Value;

namespace FizzBuzzService.Type
{
    public abstract partial class FizzBuzzType : Enumeration
    {
        public static FizzBuzzType Standard = new TypeStandard();
        public static FizzBuzzType One = new Type01();
        public static FizzBuzzType Two = new Type02();
        public static FizzBuzzType Three = new Type03();
        public static FizzBuzzType Four = new Type04();
        public static FizzBuzzType Five = new Type05();

        public virtual FizzBuzzValue Generate(int v)
        {
            var number = new Number(v);
            return number.CanDivideThreeAndFive() ? new FizzBuzzValue("FizzBuzz", number.Value) :
                number.CanDivideFive() ? new FizzBuzzValue("Buzz", number.Value) :
                number.CanDivideThree() ? new FizzBuzzValue("Fizz", number.Value) :
                new FizzBuzzValue(number.ToString(), number.Value);
        }
    }
}