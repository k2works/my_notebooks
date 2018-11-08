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

        public override bool Equals(object obj)
        {
            if (ReferenceEquals(this, obj))
            {
                return true;
            }

            if (ReferenceEquals(obj, null))
            {
                return false;
            }

            throw new NotImplementedException();
        }

        public override int GetHashCode() => throw new NotImplementedException();

        public static bool operator ==(Enumeration left, Enumeration right)
        {
            if (ReferenceEquals(left, null))
            {
                return ReferenceEquals(right, null);
            }

            return left.Equals(right);
        }

        public static bool operator !=(Enumeration left, Enumeration right)
        {
            return !(left == right);
        }

        public static bool operator <(Enumeration left, Enumeration right)
        {
            return ReferenceEquals(left, null) ? !ReferenceEquals(right, null) : left.CompareTo(right) < 0;
        }

        public static bool operator <=(Enumeration left, Enumeration right)
        {
            return ReferenceEquals(left, null) || left.CompareTo(right) <= 0;
        }

        public static bool operator >(Enumeration left, Enumeration right)
        {
            return !ReferenceEquals(left, null) && left.CompareTo(right) > 0;
        }

        public static bool operator >=(Enumeration left, Enumeration right)
        {
            return ReferenceEquals(left, null) ? ReferenceEquals(right, null) : left.CompareTo(right) >= 0;
        }
    }

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

    public abstract class ValueObject
    {
        protected abstract IEnumerable<object> GetAtomicValues();

        public override bool Equals(object obj)
        {
            if (obj == null || obj.GetType() != GetType())
            {
                return false;
            }

            ValueObject other = (ValueObject) obj;
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
        private readonly List<FizzBuzzValue> _fizzBuzzValueCollection;

        public FizzBuzzValues(List<FizzBuzzValue> fizzBuzzValueCollection) =>
            _fizzBuzzValueCollection = fizzBuzzValueCollection;

        public FizzBuzzValues Add(FizzBuzzValue fizzBuzzValue)
        {
            var result = new List<FizzBuzzValue>(_fizzBuzzValueCollection) {fizzBuzzValue};
            return new FizzBuzzValues(result);
        }

        public string[] ArrayValue()
        {
            var result = new string[_fizzBuzzValueCollection.Count];
            var i = 0;
            foreach (var each in _fizzBuzzValueCollection)
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
        void Execute(int arg);
    }

    public class FizzBuzzValueCommand : ICommand
    {
        private readonly FizzBuzzType _type;
        private FizzBuzzValue _value;

        public FizzBuzzValueCommand(FizzBuzzType type)
        {
            _type = type;
        }

        public void Execute(int number)
        {
            _value = _type.Generate(number);
        }

        public FizzBuzzValue GetResult()
        {
            return _value;
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

        public void Execute(int count)
        {
            foreach (var i in Enumerable.Range(1, count))
            {
                var fizzBuzzValue = _type.Generate(i);
                _values = _values.Add(fizzBuzzValue);
            }
        }

        public string[] GetResult()
        {
            return _values.ArrayValue();
        }
    }
}