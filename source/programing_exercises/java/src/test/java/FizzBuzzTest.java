import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class FizzBuzzTest {
    private FizzBuzz _fizzBuzz;
    private FizzBuzzType _typeNormal;
    private FizzBuzzType _typeOne;
    private FizzBuzzType _typeTwo;
    private FizzBuzzType _typeThree;
    private FizzBuzzType _typeFour;
    private FizzBuzzType _typeFive;

    @BeforeEach
    void init() {
        _fizzBuzz = new FizzBuzz();
        _typeNormal = FizzBuzzType.valueOf("normal");
        _typeOne = FizzBuzzType.valueOf("one");
        _typeTwo = FizzBuzzType.valueOf("two");
        _typeThree = FizzBuzzType.valueOf("three");
        _typeFour = FizzBuzzType.valueOf("four");
        _typeFive = FizzBuzzType.valueOf("five");
    }    
    @Test
    public void 数が3ならばFizzを返す() {   
        assertEquals("Fizz", _typeNormal.generate(3));
    }
    @Test
    public void 数が5ならばBuzzをかえす() {
        assertEquals("Buzz", _typeNormal.generate(5));
    }    
    @Test
    public void 数が15ならばFizzBuzzを返す() {        
        assertEquals("FizzBuzz", _typeNormal.generate(15));
    }
    @Test
    public void 数が1ならば1を返す() {        
        assertEquals("1", _typeNormal.generate(1));
    }
    @Test
    public void 数が101ならば101を返す() {        
        assertEquals("101", _typeNormal.generate(101));
    }
    @Test
    public void 回数を5回繰り返し実行したならば配列を返す() {
        String[] expected = {"1","2","Fizz","4","Buzz"};
        assertArrayEquals(expected, _fizzBuzz.iterate(5));
    }
    @Test
    public void 回数を10回繰り返し実行したならば配列を返す() {
        String[] expected = {"1","2","Fizz","4","Buzz", "Fizz", "7", "8", "Fizz", "Buzz"};
        assertArrayEquals(expected, _fizzBuzz.iterate(10));
    }    
    @Test
    public void タイプ１は数を返す() {           
        assertEquals("3", _typeOne.generate(3));
    }
    @Test
    public void タイプ２はFizzを返す() {         
        assertEquals("Fizz", _typeTwo.generate());
    }
    @Test
    public void タイプ３はBuzzを返す() {           
        assertEquals("Buzz", _typeThree.generate());
    }    
    @Test
    public void タイプ４は大文字の値を返す() { 
        FizzBuzzType type = _typeFour;
        assertEquals("FIZZ", type.generate(3));        
        assertEquals("BUZZ", type.generate(5));
        assertEquals("FIZZBUZZ", type.generate(15));
    } 
    @Test
    public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す() {                
        FizzBuzzType type = _typeFive;
        assertEquals("Fizz", type.generate(2));        
        assertEquals("Buzz", type.generate(3));             
        assertEquals("FIZZBUZZ", type.generate(6));        
    } 
    @Test
    public void 上記以外のは通常のFizzBuzzパターンを返す() {  
        FizzBuzzType type = _typeNormal;
        assertEquals("Fizz", type.generate(3));    
        assertEquals("Buzz", type.generate(5));                
        assertEquals("FizzBuzz", type.generate(15));        
    }    
}