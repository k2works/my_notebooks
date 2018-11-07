using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

namespace FizzBuzzService
{
    public abstract class Enumeration : IComparable
    {
        public int CompareTo(object obj)
        {
            throw new NotImplementedException();
        }
    }

    public abstract class FizzBuzzType : Enumeration
    {
        public static FizzBuzzType Standard = new TypeStandard();
        public static FizzBuzzType One = new Type01();
        public static FizzBuzzType Two = new Type02();
        public static FizzBuzzType Three = new Type03();
        public static FizzBuzzType Four = new Type04();
        public static FizzBuzzType Five = new Type05();
        protected FizzBuzzType()
        {
        }

        protected string _value;

        public String Value { get { return this._value; } }

        public virtual String generate(int number)
        {
            String value = number.ToString();

            if (number % 3 == 0 && number % 5 == 0)
            {
                value = "FizzBuzz";
            }
            else if (number % 5 == 0)
            {
                value = "Buzz";
            }
            else if (number % 3 == 0)
            {
                value = "Fizz";
            }

            return value;
        }        

        private class Type01 : FizzBuzzType
        {
            public Type01()
            {
            }

            public override String generate(int number)
            {
                return number.ToString();
            }
        }

        private class Type02 : FizzBuzzType
        {
            public Type02()
            {
            }

            public override String generate(int number)
            {
                return "Fizz";
            }
        }

        private class Type03 : FizzBuzzType
        {
            public Type03() { }

            public override String generate(int number)
            {
                return "Buzz";
            }
        }

        private class Type04 : FizzBuzzType
        {
            public override String generate(int number)
            {
                String value = base.generate(number);

                return value.ToUpper();
            }
        }

        private class Type05 : FizzBuzzType
        {
            public override String generate(int number)
            {
                String value = number.ToString();

                if (number % 2 == 0 && number % 3 == 0)
                {
                    value = "FIZZBUZZ";
                }
                else if (number % 2 == 0)
                {
                    value = "Fizz";
                }
                else if (number % 3 == 0)
                {
                    value = "Buzz";
                }
                else
                {
                    value = number.ToString();
                }

                return value;
            }
        }

        private class TypeStandard : FizzBuzzType { }
    }

    public class FizzBuzz
    {
        private String _value;
        private String[] _values;
        private FizzBuzzType _type;

        public String Value
        {
            get { return _value; }
        }
        public String[] Values
        {
            get { return _values; }
        }
        public FizzBuzz() { }
        public FizzBuzz(FizzBuzzType type)
        {
            _type = type;
        }
        public void generate(int number)
        {
            this._value = _type.generate(number);
        }

        public void iterate(int count)
        {
            String[] array = new String[count];
            FizzBuzzType type = FizzBuzzType.Standard;
            FizzBuzz fizzBuzz = new FizzBuzz(type);

            for (var i = 0; i < count; i = i + 1)
            {
                fizzBuzz.generate(i + 1);
                array[i] = fizzBuzz.Value;
            }
            this._values = array;
        }
    }
}
