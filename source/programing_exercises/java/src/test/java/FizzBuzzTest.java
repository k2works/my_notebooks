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
    public void 回数を10回繰り返し実行したならば配列を返す() {
        String[] expected = {"1","2","Fizz","4","Buzz", "Fizz", "7", "8", "Fizz", "Buzz"};
        String[] actual = FizzBuzz.iterate(10);
        _fizzBuzzData.setValues(actual);
        assertArrayEquals(expected, _fizzBuzzData.getValues());
    }    
    @Test
    public void タイプ１は数を返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(3,1));
        assertEquals("3", _fizzBuzzData.getValue());
    }
    @Test
    public void タイプ２はFizzを返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(5,2));
        assertEquals("Fizz", _fizzBuzzData.getValue());
    }
    @Test
    public void タイプ３はBuzzを返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(3,3));
        assertEquals("Buzz", _fizzBuzzData.getValue());
    }    
    @Test
    public void タイプ４は大文字の値を返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(3,4));
        assertEquals("FIZZ", _fizzBuzzData.getValue());
        _fizzBuzzData.setValue(FizzBuzz.generate(5,4));
        assertEquals("BUZZ", _fizzBuzzData.getValue());        
        _fizzBuzzData.setValue(FizzBuzz.generate(15,4));
        assertEquals("FIZZBUZZ", _fizzBuzzData.getValue());        
    } 
    @Test
    public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(2,5));
        assertEquals("Fizz", _fizzBuzzData.getValue());
        _fizzBuzzData.setValue(FizzBuzz.generate(3,5));
        assertEquals("Buzz", _fizzBuzzData.getValue());        
        _fizzBuzzData.setValue(FizzBuzz.generate(6,5));
        assertEquals("FIZZBUZZ", _fizzBuzzData.getValue());        
    } 
    @Test
    public void 上記以外のは通常のFizzBuzzパターンを返す() {
        _fizzBuzzData.setValue(FizzBuzz.generate(3,6));
        assertEquals("Fizz", _fizzBuzzData.getValue());
        _fizzBuzzData.setValue(FizzBuzz.generate(5,6));
        assertEquals("Buzz", _fizzBuzzData.getValue());        
        _fizzBuzzData.setValue(FizzBuzz.generate(15,6));
        assertEquals("FizzBuzz", _fizzBuzzData.getValue());        
    }    
}