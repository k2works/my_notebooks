class FizzBuzz {
    public static String generate(int number) {
        String value = Integer.toString(number);

        if (number % 3 == 0 && number % 5 == 0) {
            value = "FizzBuzz";    
        } else if (number % 3 == 0) {
            value = "Fizz";
        } else if (number % 5 == 0) {
            value = "Buzz";
        }

        return value;
    }
}
