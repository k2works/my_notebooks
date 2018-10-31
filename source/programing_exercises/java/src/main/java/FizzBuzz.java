interface IType{
    String generate();
}

class Type01 implements IType {
    private String _number;

    Type01(int number) {
        this._number = Integer.toString(number);
    }

    public String generate() {
        return this._number;
    }
}

class Type02 implements IType {
    public String generate() {
        return "Fizz";
    }
}

class Type03 implements IType {
    public String generate() {
        return "Buzz";
    }
}

class Type04 implements IType {
    private Integer _number;

    Type04(int number) {
        this._number = number;
    }

    public String generate() {
        if (this._number % 3 == 0 && this._number % 5 == 0) {
            return "FIZZBUZZ";
        } else if (this._number % 3 == 0) {
            return "FIZZ";
        } else if (this._number % 5 == 0) {
            return "BUZZ";
        }
        return Integer.toString(this._number);
    }
}

class Type05 implements IType {
    private Integer _number;

    Type05(int number) {
        this._number = number;
    }

    public String generate() {
        if (this._number % 2 == 0 && this._number % 3 == 0) {
            return "FIZZBUZZ";
        } else if (this._number % 2 == 0) {
            return "Fizz";
        } else if (this._number % 3 == 0) {
            return "Buzz";
        }
        return Integer.toString(this._number);
    }
}

class TypeNormal implements IType {
    private Integer _number;

    TypeNormal(int number) {
        this._number = number;
    }

    public String generate() {
        if (this._number % 3 == 0 && this._number % 5 == 0) {
            return "FizzBuzz";
        } else if (this._number % 3 == 0) {
            return "Fizz";
        } else if (this._number % 5 == 0) {
            return "Buzz";
        }
        return Integer.toString(this._number);
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

    public String generate(IType type) {
        return type.generate();
    }

    public String[] iterate(int count) {
        this._values = new String[count];
        FizzBuzz fizzBuzz = new FizzBuzz();

        for (int i = 0; i < count; i = i + 1) {
            IType type = new TypeNormal(i + 1);
            this._values[i] = fizzBuzz.generate(type);
        }

        return this._values;
    }
}
