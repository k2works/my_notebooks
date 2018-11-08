namespace FizzBuzzService
{
    public class Number
    {
        public Number(int number)
        {
            Value = number;
        }

        public int Value { get; }

        public override string ToString()
        {
            return Value.ToString();
        }

        public bool CanDivideThree()
        {
            return Value % 3 == 0;
        }

        public bool CanDivideFive()
        {
            return Value % 5 == 0;
        }

        public bool CanDivideThreeAndFive()
        {
            return Value % 3 == 0 && Value % 5 == 0;
        }

        public bool CanDivideTwo()
        {
            return Value % 2 == 0;
        }

        public bool CanDivideTwoAndThree()
        {
            return Value % 2 == 0 && Value % 3 == 0;
        }
    }
}