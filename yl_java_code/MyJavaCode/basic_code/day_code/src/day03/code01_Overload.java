package day03;

public class code01_Overload {
    public static void main(String[] args) {
        System.out.println(sunTwo(10,20));
        System.out.println(sunThree(10, 20, 30));
        System.out.println(sunFour(10, 20, 30, 40));
        System.out.println(sun(10, 20));
        System.out.println(sun(10, 20, 30));
        System.out.println(sun(10, 20, 30, 40));

    }

    public static int sunTwo(int a, int b){
        return a + b;
    }

    public static int sunThree(int a, int b, int c){
        return a + b + c;
    }

    public static int sunFour(int a, int b, int c, int d){
        return a + b + c + d;
    }

    public static int sun(int a, int b){
        System.out.println("sun_有2个参数");
        return a + b;
    }

    public static int sun(int a, int b, int c){
        System.out.println("sun_有3个参数");
        return a + b + c;
    }

    public static int sun(int a, int b, int c, int d){
        System.out.println("sun_有4个参数");
        return a + b + c + d;
    }
}
