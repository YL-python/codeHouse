package TestCode.Test;

import TestCode.MyCode.Calculator;
import org.junit.Assert;
import org.junit.Test;

public class CalculatorTest {
    @Test
    public void testAdd(){
        Calculator c = new Calculator();
        int result = c.add(1,2);
//        System.out.println(result);
        Assert.assertEquals(2, result);
    }

    @Test
    public void testSub(){
        Calculator c = new Calculator();
        int result = c.sub(1,2);
//        System.out.println(result);
        Assert.assertEquals(-1, result);
    }
}
