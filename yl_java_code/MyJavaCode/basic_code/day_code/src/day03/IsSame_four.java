package day03;

public class IsSame_four {
    public static void main(String[] args) {
        byte a = 5;
        byte b = 7;
        System.out.println(IsSame(a, b));
        System.out.println(IsSame((short) 20, (short) 30));
        System.out.println(IsSame(11, 12));
        System.out.println(IsSame(10L, 10L));
    }

    public static boolean IsSame(byte a, byte b){
        System.out.println("=====byte=====");
        boolean same;
        if(a == b){
            same = true;
        }else{
            same = false;
        }
        return same;
    }

    public static boolean IsSame(short a, short b){
        System.out.println("=====short=====");
        boolean same = a == b ? true : false;
        return  same;
    }

    public static boolean IsSame(int a, int b){
        System.out.println("=====int=====");
        return a == b;
    }

    public static boolean IsSame(long a, long b){
        System.out.println("=====long=====");
        if(a == b){
            return true;
        }else{
            return false;
        }
    }
}
