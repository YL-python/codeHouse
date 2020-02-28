package Exception_code.MyselfException;

import java.util.Scanner;

public class textdemo {
    static String[] usernames = { "aaa", "bbb", "ccc" };
    public static void main(String[] args) {
        System.out.print("取一个名字把：");
        String username = new Scanner(System.in).next();
        try {
            chackusername(username);
        } catch (MyException e) {
            e.printStackTrace();
        }
    }
    public static void chackusername(String name) throws MyException {
        for (String username : usernames) {
            if (name.equals(username)){
                throw new MyException("名称已经被注册了哦！");
            }
        }
        System.out.println("注册成功！");
    }
}
