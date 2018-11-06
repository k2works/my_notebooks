using System;

namespace FizzBuzzService
{
    public class FizzBuzz
    {
        public static String generate(int number)
        {            
            String value = number.ToString();
            
            if (number % 3 == 0 && number % 5 == 0) {
                value = "FizzBuzz";
            } else if (number % 5 == 0) {
                value = "Buzz";
            } else if (number % 3 == 0) {
                value = "Fizz";
            }

            return value;
        }

        public static String[] iterate(int count)
        {            
            String[] array = new String[count];

            for (var i = 0; i < count; i = i + 1) {
                array[i] = FizzBuzz.generate(i + 1);
            }

            return array;
        }
    }
}
