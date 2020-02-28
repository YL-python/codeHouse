package code_Thread.day02Thread;

public class Demo01 {
    public static void main(String[] args) {
        for(int i = 0; i<20;i++){
            System.out.println("main01" + "--->" + i);
        }
        Person per1 = new Person();
        per1.start();
        System.out.println("============");
        for(int i = 0; i<20;i++){
            System.out.println("main02" + "--->" + i);
        }
    }
}
