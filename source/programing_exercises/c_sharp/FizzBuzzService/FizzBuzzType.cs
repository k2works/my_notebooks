namespace FizzBuzzService
{
    public abstract class FizzBuzzType : Enumeration
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

        private class Type01 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int number)
            {
                var value = number.ToString();
                return new FizzBuzzValue(value, number);
            }
        }

        private class Type02 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int number) => new FizzBuzzValue("Fizz", number);
        }

        private class Type03 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int number) => new FizzBuzzValue("Buzz", number);
        }

        private class Type04 : FizzBuzzType
        {
            public override FizzBuzzValue Generate(int number)
            {
                var value = base.Generate(number);

                return new FizzBuzzValue(value.Value.ToUpper(), number);
            }
        }

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

        private class TypeStandard : FizzBuzzType
        {
        }
    }
}