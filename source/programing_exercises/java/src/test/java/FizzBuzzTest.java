import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class FizzBuzzTest {
    private FizzBuzzData _fizzBuzzData;
    @BeforeEach
    void init() {
        _fizzBuzzData = new FizzBuzzData();
    }    
    @Test
    public void 数が3ならばFizzを返す() {    
        _fizzBuzzData.setValue(FizzBuzz.generate(3));
        assertEquals("Fizz", _fizzBuzzData.getValue());
    }
    @Test
    public void 数が5ならばBuzzをかえす() {
        _fizzBuzzData.setValue(FizzBuzz.generate(5));
        assertEquals("Buzz", _fizzBuzzData.getValue());
    }    
    @Test
    public void 数が15ならばFizzBuzzを返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(15));
        assertEquals("FizzBuzz", _fizzBuzzData.getValue());
    }
    @Test
    public void 数が1ならば1を返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(1));
        assertEquals("1", _fizzBuzzData.getValue());
    }
    @Test
    public void 数が101ならば101を返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(101));
        assertEquals("101", _fizzBuzzData.getValue());
    }
    @Test
    public void 回数を5回繰り返し実行したならば配列を返す() {
        String[] expected = {"1","2","Fizz","4","Buzz"};
        String[] actual = FizzBuzz.iterate(5);
        _fizzBuzzData.setValues(actual);
        assertArrayEquals(expected, _fizzBuzzData.getValues());
    }

    @Test
    public void test10回繰り返し実行したならば配列を返す() {
        String[] expected = {"1","2","Fizz","4","Buzz", "Fizz", "7", "8", "Fizz", "Buzz"};
        String[] actual = FizzBuzz.iterate(10);
        _fizzBuzzData.setValues(actual);
        assertArrayEquals(expected, _fizzBuzzData.getValues());
    }    
}