class FizzBuzz {
    private String _value;
    private String _values[];

    public String getValue(){
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

    public String generate(int number, int flg) {
        this._value = Integer.toString(number);

        switch(flg) {
            case 1:            
                break;    
            case 2:
                this._value = "Fizz";
                break;
            case 3:
                this._value = "Buzz";
                break;
            case 4:
                        if (number % 3 == 0 && number % 5 == 0) {
                            this._value = "FIZZBUZZ";    
                        } else if (number % 3 == 0) {
                            this._value = "FIZZ";
                        } else if (number % 5 == 0) {
                            this._value = "BUZZ";
                        }
                        break;
            case 5:
                        if (number % 2 == 0 && number % 3 == 0) {
                            this._value = "FIZZBUZZ";    
                        } else if (number % 2 == 0) {
                            this._value = "Fizz";
                        } else if (number % 3 == 0) {
                            this._value = "Buzz";
                        }
                        break;
            default:
                        if (number % 3 == 0 && number % 5 == 0) {
                            this._value = "FizzBuzz";    
                        } else if (number % 3 == 0) {
                            this._value = "Fizz";
                        } else if (number % 5 == 0) {
                            this._value = "Buzz";
                        }                        
                        break;
        }    

        return this._value;    
    }    

	public String[] iterate(int count) {
        this._values = new String[count];
        FizzBuzz fizzBuzz = new FizzBuzz();

        for(int i = 0; i < count; i = i + 1) {
            this._values[i] = fizzBuzz.generate(i + 1);
        }
        
        return this._values;
	}
}
