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

    String generate() {
        return type.generate();
    }

    String generate(int number) {
        return type.generate(number);
    }    
}

interface IType{
    String generate();
    String generate(int number);
}

class Type01 implements IType {
    private String _number;

    Type01(){};
    Type01(int number) {
        this._number = Integer.toString(number);
    }

    public String generate() {
        return this._number;
    }

    @Override
    public String generate(int number) {
        return Integer.toString(number);
    }
}

class Type02 implements IType {
    public String generate() {
        return "Fizz";
    }

    @Override
    public String generate(int number) {
        return "Fizz";
    }
}

class Type03 implements IType {
    public String generate() {
        return "Buzz";
    }

    @Override
    public String generate(int number) {
        return null;
    }
}

class Type04 implements IType {
    private Integer _number;

    Type04() {};
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

    @Override
    public String generate(int number) {
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
    private Integer _number;

    Type05() {};
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

    @Override
    public String generate(int number) {
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
    private Integer _number;

    TypeNormal() {};
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

    @Override
    public String generate(int number) {
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
