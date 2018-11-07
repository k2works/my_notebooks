﻿using System;
using System.Collections.Generic;

namespace FizzBuzzService
{
    public abstract class Type
    {
        protected string _value;

        public String Value { get { return this._value; } }

        public virtual void generate(int number)
        {
            this._value = number.ToString();

            if (number % 3 == 0 && number % 5 == 0)
            {
                this._value = "FizzBuzz";
            }
            else if (number % 5 == 0)
            {
                this._value = "Buzz";
            }
            else if (number % 3 == 0)
            {
                this._value = "Fizz";
            }
        }
    }
    public class Type01 : Type
    {
        public Type01()
        {
        }

        public override void generate(int number)
        {
            this._value = number.ToString();
        }
    }

    public class Type02 : Type
    {
        public Type02()
        {
        }

        public override void generate(int number)
        {
            this._value = "Fizz";
        }
    }

    public class Type03 : Type
    {
        public Type03() { }

        public override void generate(int number)
        {
            this._value = "Buzz";
        }
    }

    public class Type04 : Type
    {
        public override void generate(int number)
        {
            base.generate(number);
            
            this._value = this._value.ToUpper();
        }
    }

    public class Type05 : Type
    {
        public override void generate(int number)
        {
            if (number % 2 == 0 && number % 3 == 0)
            {
                this._value = "FIZZBUZZ";
            }
            else if (number % 2 == 0)
            {
                this._value = "Fizz";
            }
            else if (number % 3 == 0)
            {
                this._value = "Buzz";
            }
            else
            {
                this._value = number.ToString();
            }
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
        public FizzBuzz()
        {
            _type = new TypeStandard();
        }
        public void generate(int number)
        {
            _type.generate(number);
            this._value = _type.Value;
        }

        public void iterate(int count)
        {
            String[] array = new String[count];
            FizzBuzz fizzBuzz = new FizzBuzz();

            for (var i = 0; i < count; i = i + 1)
            {
                fizzBuzz.generate(i + 1);
                array[i] = fizzBuzz.Value;
            }
            this._values = array;
        }
    }
}
