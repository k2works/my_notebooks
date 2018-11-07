using System;
using System.Collections.Generic;

namespace FizzBuzzService
{
    public abstract class Type
    {
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
    }
    public class Type01 : Type
    {
        public Type01()
        {
        }

        public override String generate(int number)
        {
            return number.ToString();
        }
    }

    public class Type02 : Type
    {
        public Type02()
        {
        }

        public override String generate(int number)
        {
            return "Fizz";
        }
    }

    public class Type03 : Type
    {
        public Type03() { }

        public override String generate(int number)
        {
            return "Buzz";
        }
    }

    public class Type04 : Type
    {
        public override String generate(int number)
        {
            String value = base.generate(number);
            
            return value.ToUpper();
        }
    }

    public class Type05 : Type
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

    public class TypeStandard : Type { }

    public class FizzBuzz
    {
        private String _value;
        private String[] _values;
        private Type _type;

        public String Value
        {
            get { return _value; }
        }
        public String[] Values
        {
            get { return _values; }
        }
        public FizzBuzz() { }        
        public FizzBuzz(Type type)
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
            Type type = new TypeStandard();
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
