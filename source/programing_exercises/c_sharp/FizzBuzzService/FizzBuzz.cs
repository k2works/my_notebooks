using System;
using System.Collections.Generic;
using System.Linq;

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
        protected FizzBuzzType() { }

        public virtual FizzBuzzValue generate(int number)
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

            return new FizzBuzzValue(value, number);
        }

        private class Type01 : FizzBuzzType
        {
            public Type01()
            {
            }

            public override FizzBuzzValue generate(int number)
            {
                var value = number.ToString();
                return new FizzBuzzValue(value, number);
            }
        }

        private class Type02 : FizzBuzzType
        {
            public Type02()
            {
            }

            public override FizzBuzzValue generate(int number)
            {
                return new FizzBuzzValue("Fizz", number);
            }
        }

        private class Type03 : FizzBuzzType
        {
            public Type03() { }

            public override FizzBuzzValue generate(int number)
            {
                return new FizzBuzzValue("Buzz", number);
            }
        }

        private class Type04 : FizzBuzzType
        {
            public override FizzBuzzValue generate(int number)
            {
                FizzBuzzValue value = base.generate(number);

                return new FizzBuzzValue(value.Value.ToUpper(), number);
            }
        }

        private class Type05 : FizzBuzzType
        {
            public override FizzBuzzValue generate(int number)
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

                return new FizzBuzzValue(value, number);
            }
        }

        private class TypeStandard : FizzBuzzType { }
    }

    public abstract class ValueObject
    {
        protected static bool EqualOperator(ValueObject left, ValueObject right)
        {
            if (ReferenceEquals(left, null) ^ ReferenceEquals(right, null))
            {
                return false;
            }
            return ReferenceEquals(left, null) || left.Equals(right);
        }

        protected static bool NotEqualOperator(ValueObject left, ValueObject right)
        {
            return !(EqualOperator(left, right));
        }

        protected abstract IEnumerable<object> GetAtomicValues();

        public override bool Equals(object obj)
        {
            if (obj == null || obj.GetType() != GetType())
            {
                return false;
            }

            ValueObject other = (ValueObject)obj;
            IEnumerator<object> thisValues = GetAtomicValues().GetEnumerator();
            IEnumerator<object> otherValues = other.GetAtomicValues().GetEnumerator();
            while (thisValues.MoveNext() && otherValues.MoveNext())
            {
                if (ReferenceEquals(thisValues.Current, null) ^ ReferenceEquals(otherValues.Current, null))
                {
                    return false;
                }

                if (thisValues.Current != null && !thisValues.Current.Equals(otherValues.Current))
                {
                    return false;
                }
            }
            return !thisValues.MoveNext() && !otherValues.MoveNext();
        }

        public override int GetHashCode()
        {
            return GetAtomicValues()
            .Select(x => x != null ? x.GetHashCode() : 0)
            .Aggregate((x, y) => x ^ y);
        }
    }

    public class FizzBuzzValues
    {
        private List<FizzBuzzValue> _fizzBuzzValues;

        public FizzBuzzValues(List<FizzBuzzValue> fizzBuzzValues)
        {
            _fizzBuzzValues = fizzBuzzValues;
        }

        public FizzBuzzValues add(FizzBuzzValue fizzBuzzValue)
        {
            var result = new List<FizzBuzzValue>(_fizzBuzzValues);
            result.Add(fizzBuzzValue);
            return new FizzBuzzValues(result);
        }

        public List<FizzBuzzValue> getCollection()
        {
            return this._fizzBuzzValues;
        }

        public string[] arrayValue()
        {
            string[] result = new string[_fizzBuzzValues.Count];
            var i = 0;
            foreach (FizzBuzzValue each in _fizzBuzzValues)
            {
                result[i] = each.Value;
                i = i + 1;
            }
            return result;
        }
    }

    public class FizzBuzzValue : ValueObject
    {
        public string Value { get; }
        public int Number { get; }

        private FizzBuzzValue() { }

        public FizzBuzzValue(string value, int number)
        {
            Value = value;
            Number = number;
        }

        protected override IEnumerable<object> GetAtomicValues()
        {
            yield return Value;
            yield return Number;
        }
    }

    public interface ICommand
    {
        void execute(int arg);        
    }

    public class FizzBuzzValueCommand : ICommand
    {
        private readonly FizzBuzzType _type;
        private FizzBuzzValue _value;

        public FizzBuzzValueCommand(FizzBuzzType type)
        {
            _type = type;
        }

        public void execute(int number)
        {
            _value = _type.generate(number);
        }

        public FizzBuzzValue getResult()
        {
            return this._value;
        }
    }

    public class FizzBuzzValuesCommand : ICommand
    {
        private readonly FizzBuzzType _type;
        private FizzBuzzValues _values;

        public FizzBuzzValuesCommand(FizzBuzzType type)
        {
            _type = type;
            var list = new List<FizzBuzzValue>();
            _values = new FizzBuzzValues(list);            
        }

        public void execute(int count)
        {
            foreach (var i in Enumerable.Range(1, count))
            {
                FizzBuzzValue fizzBuzzValue = _type.generate(i);
                this._values = this._values.add(fizzBuzzValue);
            }
        }

        public string[] getResult()
        {
            return this._values.arrayValue();
        }
    }
}
