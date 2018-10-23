import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class FizzBuzzTest {
    @Test
    public void test3ならばFizzを返す() {
        assertEquals("Fizz", FizzBuzz.generate(3));
    }
    @Test
    public void test5ならばBuzzをかえす() {
        assertEquals("Buzz", FizzBuzz.generate(5));
    }    
    @Test
    public void test15ならばFizzBuzzか返す() {
        assertEquals("FizzBuzz", FizzBuzz.generate(15));
    }
}