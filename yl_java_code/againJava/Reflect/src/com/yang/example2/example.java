package com.yang.example2;

// 需求，给定任意对象，获取对象中的值并写到文件中

import java.util.Date;

public class example {

    public static void main(String[] args) throws IllegalAccessException {
        User user = new User("zhangsan", "12334", 18);
        People people = new People("xiaomin", 18, "110", new Date());
        Utils.getAll(user);
        Utils.getAll(people);

        Utils.getAllWithAnno(people);

    }
}
