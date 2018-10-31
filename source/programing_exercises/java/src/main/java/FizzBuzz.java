class Type01 {
    private String _number;

    Type01(int number) {
        this._number = Integer.toString(number);
    }

    public String generate() {
        return this._number;
    }
}

class Type02 {
    public String generate() {
        return "Fizz";
    }
}

class Type03 {
    public String generate() {
        return "Buzz";
    }
}

class Type04 {
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

class Type05 {
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

class TypeNormal {
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

    public String generate(int number) {
        this._value = Integer.toString(number);

        if (number % 3 == 0 && number % 5 == 0) {
            this._value = "FizzBuzz";
        } else if (number % 3 == 0) {
            this._value = "Fizz";
        } else if (number % 5 == 0) {
            this._value = "Buzz";
        }

        return this._value;
    }

    public String generate(Type01 type) {
        return type.generate();
    }

    public String generate(Type02 type) {
        return type.generate();
    }

    public String generate(Type03 type) {
        return type.generate();
    }

    public String generate(Type04 type) {
        return type.generate();
    }

    public String generate(Type05 type) {
        return type.generate();
    }

    public String generate(TypeNormal type) {
        return type.generate();
    }


    public String[] iterate(int count) {
        this._values = new String[count];
        FizzBuzz fizzBuzz = new FizzBuzz();

        for (int i = 0; i < count; i = i + 1) {
            this._values[i] = fizzBuzz.generate(i + 1);
        }

        return this._values;
    }
}
