package code_Thread.MainThread;

public class Demo01 {
    public static void main(String[] args) {
        Person per1 = new Person("小明");
        per1.run();

        //System.out.println(0/0);  // Exception in thread "main"

        Person per2 = new Person("小红");
        per2.run();
    }
}
