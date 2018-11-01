import java.util.ArrayList;
import java.util.List;

interface IType {
    String generate(int number);
}

class Type01 implements IType {
    @Override
    public String generate(int number) {
        String value = Integer.toString(number);
        FizzBuzzValue fizzBzuuValue = new FizzBuzzValue(number, value);
        return fizzBzuuValue.getValue();
    }
}

class Type02 implements IType {
    @Override
    public String generate(int number) {
        FizzBuzzValue fizzBzuuValue = new FizzBuzzValue(number, "Fizz");
        return fizzBzuuValue.getValue();
    }
}

class Type03 implements IType {
    @Override
    public String generate(int number) {
        FizzBuzzValue fizzBzuuValue = new FizzBuzzValue(number, "Buzz");
        return fizzBzuuValue.getValue();
    }
}

class Type04 implements IType {
    @Override
    public String generate(int number) {
        String value = this.judge(number);
        FizzBuzzValue fizzBzuuValue = new FizzBuzzValue(number, value);
        return fizzBzuuValue.getValue();        
    }

    private String judge(int number) {
        if (number % 3 == 0 && number % 5 == 0) {
            return "FIZZBUZZ";
        } else if (number % 3 == 0) {
            return "FIZZ";
        } else if (number % 5 == 0) {
            return "BUZZ";
        }
        return Integer.toString(number);
    }
}

class Type05 implements IType {
    @Override
    public String generate(int number) {
        String value = this.judge(number);
        FizzBuzzValue fizzBzuuValue = new FizzBuzzValue(number, value);
        return fizzBzuuValue.getValue();        
    }

    private String judge(int number) {
        if (number % 2 == 0 && number % 3 == 0) {
            return "FIZZBUZZ";
        } else if (number % 2 == 0) {
            return "Fizz";
        } else if (number % 3 == 0) {
            return "Buzz";
        }
        return Integer.toString(number);
    }
}

class TypeNormal implements IType {
    @Override
    public String generate(int number) {
        String value = this.judge(number);
        FizzBuzzValue fizzBzuuValue = new FizzBuzzValue(number, value);
        return fizzBzuuValue.getValue();                
    }

    private String judge(int number) {
        if (number % 3 == 0 && number % 5 == 0) {
            return "FizzBuzz";
        } else if (number % 3 == 0) {
            return "Fizz";
        } else if (number % 5 == 0) {
            return "Buzz";
        }
        return Integer.toString(number);
    }
}

enum FizzBuzzType {
    one(new Type01()),
    two(new Type02()),
    three(new Type03()),
    four(new Type04()),
    five(new Type05()),
    normal(new TypeNormal());

    private IType type;

    private FizzBuzzType(IType type ) {
        this.type = type;
    }

    String generate(int number) {
        return type.generate(number);
    }    
}

class FizzBuzzValue {
    private Integer _number;    
    private String _value;

    FizzBuzzValue(Integer number, String value) {
        this._number = number;
        this._value = value;
    }

    public Integer getNumber() {
        return this._number;
    }    

    public String getValue() {
        return this._value;
    }    
}

class FizzBuzzValues {
    List<FizzBuzzValue> _fizzBzuuValues;

    public FizzBuzzValues(boolean add) {
    }

    FizzBuzzValues add(FizzBuzzValue fizzBuzzValue) {
        List<FizzBuzzValue> result = new ArrayList<>(_fizzBzuuValues);
        return new FizzBuzzValues(result.add(fizzBuzzValue));
    }

    String[] arrayValue() {
        String[] result = new String[_fizzBzuuValues.size()];
        int i = 0;
        for(FizzBuzzValue fizzBuzzValue :_fizzBzuuValues) {
            result[i] = fizzBuzzValue.getValue();
            i =+ 1;
        }
        return result;
    }
}

class FizzBuzz {
    private String _value;
    private String _values[];

    public String getValue() {
        return this._value;
    }

    public String[] getValues() {
        return this._values;
    }

    public String[] iterate(int count) {        
        this._values = new String[count];
        FizzBuzzType fizzBuzz = FizzBuzzType.valueOf("normal");

        for (int i = 0; i < count; i = i + 1) {            
            this._values[i] = fizzBuzz.generate(i + 1);
        }

        return this._values;
    }
}
