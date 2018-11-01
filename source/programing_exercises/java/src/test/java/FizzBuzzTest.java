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
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeNormal);
        command.execute(3);
        assertEquals("Fizz", command.getValue());
    }
    @Test
    public void 数が5ならばBuzzをかえす() {
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeNormal);
        command.execute(5);        
        assertEquals("Buzz", command.getValue());
    }    
    @Test
    public void 数が15ならばFizzBuzzを返す() {  
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeNormal);
        command.execute(15);        
        assertEquals("FizzBuzz", command.getValue());
    }
    @Test
    public void 数が1ならば1を返す() {  
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeNormal);
        command.execute(1);                      
        assertEquals("1", command.getValue());
    }
    @Test
    public void 数が101ならば101を返す() {      
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeNormal);
        command.execute(101);          
        assertEquals("101", command.getValue());
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
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeOne);
        command.execute(3);                                     
        assertEquals("3", command.getValue());
    }
    @Test
    public void タイプ２はFizzを返す() {       
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeTwo);
        command.execute(1);                                               
        assertEquals("Fizz", command.getValue());
    }
    @Test
    public void タイプ３はBuzzを返す() {   
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeThree);
        command.execute(1);                                               
        assertEquals("Buzz", command.getValue());
    }    
    @Test
    public void タイプ４は大文字の値を返す() { 
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeFour);
        command.execute(3);                                               
        assertEquals("FIZZ", command.getValue());        
        command.execute(5);                                               
        assertEquals("BUZZ", command.getValue());
        command.execute(15);                                               
        assertEquals("FIZZBUZZ", command.getValue());
    } 
    @Test
    public void タイプ５は２で割り切れたらFizz３で割り切れたらBuzz２と３で割り切れたならFIZZBUZZを返す() {                
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeFive);
        command.execute(2);
        assertEquals("Fizz", command.getValue());        
        command.execute(3);
        assertEquals("Buzz", command.getValue());             
        command.execute(6);        
        assertEquals("FIZZBUZZ", command.getValue());        
    } 
    @Test
    public void 上記以外のは通常のFizzBuzzパターンを返す() {  
        FizzBuzzValueCommand command = new FizzBuzzValueCommand(_typeNormal);        
        command.execute(3);
        assertEquals("Fizz", command.getValue());    
        command.execute(5);
        assertEquals("Buzz", command.getValue());                
        command.execute(15);
        assertEquals("FizzBuzz", command.getValue());        
    }    
}