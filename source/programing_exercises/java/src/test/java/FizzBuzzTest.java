import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class FizzBuzzTest {
    private FizzBuzz _fizzBuzz;
    @BeforeEach
    void init() {
        _fizzBuzz = new FizzBuzz();
    }    
    @Test
    public void 数が3ならばFizzを返す() {   
        IType type = new TypeNormal(3); 
        assertEquals("Fizz", _fizzBuzz.generate(type));
    }
    @Test
    public void 数が5ならばBuzzをかえす() {
        IType type = new TypeNormal(5);
        assertEquals("Buzz", _fizzBuzz.generate(type));
    }    
    @Test
    public void 数が15ならばFizzBuzzを返す() {
        IType type = new TypeNormal(15);
        assertEquals("FizzBuzz", _fizzBuzz.generate(type));
    }
    @Test
    public void 数が1ならば1を返す() {
        IType type = new TypeNormal(1);
        assertEquals("1", _fizzBuzz.generate(type));
    }
    @Test
    public void 数が101ならば101を返す() {
        IType type = new TypeNormal(101);
        assertEquals("101", _fizzBuzz.generate(type));
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
        IType type = new Type01(3);
        assertEquals("3", _fizzBuzz.generate(type));
    }
    @Test
    public void タイプ２はFizzを返す() { 
        FizzBuzzType type = FizzBuzzType.valueOf("two");
        assertEquals("Fizz", type.generate());
    }
    @Test
    public void タイプ３はBuzzを返す() {   
        IType type = new Type03();
        assertEquals("Buzz", _fizzBuzz.generate(type));
    }    
    @Test
    public void タイプ４は大文字の値を返す() { 
        IType type = new Type04(3);
        assertEquals("FIZZ", _fizzBuzz.generate(type));        
        type = new Type04(5);
        assertEquals("BUZZ", _fizzBuzz.generate(type));
        type = new Type04(15);
        assertEquals("FIZZBUZZ", _fizzBuzz.generate(type));
    } 
    @Test
    public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す() {        
        IType type = new Type05(2);
        assertEquals("Fizz", _fizzBuzz.generate(type));
        type = new Type05(3);
        assertEquals("Buzz", _fizzBuzz.generate(type));     
        type = new Type05(6);
        assertEquals("FIZZBUZZ", _fizzBuzz.generate(type));        
    } 
    @Test
    public void 上記以外のは通常のFizzBuzzパターンを返す() {  
        IType type = new TypeNormal(3);
        assertEquals("Fizz", _fizzBuzz.generate(type));    
        type = new TypeNormal(5);
        assertEquals("Buzz", _fizzBuzz.generate(type));                
        type = new TypeNormal(15);
        assertEquals("FizzBuzz", _fizzBuzz.generate(type));        
    }    
}