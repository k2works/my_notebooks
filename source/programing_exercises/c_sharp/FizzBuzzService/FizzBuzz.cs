using System;

namespace FizzBuzzService
{
    public class FizzBuzz
    {
        private String _value;
        private String[] _values;

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
        }        
        public void generate(int number)
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

        public void generate(int number, int type)
        {
            String value;

            switch (type)
            {
                case 1:
                    this._value = number.ToString();
                    break;
                case 2:
                    this._value = "Fizz";
                    break;
                case 3:
                    this._value = "Buzz";
                    break;
                case 4:
                    value = number.ToString();

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

                    this._value = value.ToUpper();
                    break;
                case 5:
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
                    break;
                default:     
                    value = null;        

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

                    this._value = value;
                    break;
            }            
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
