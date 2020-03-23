package com.yang.controller;

public @interface MyAnno {
    // 注解里面的属性也就是  接口中的抽象方法返回值必须是
    // 字符串，基本数据类型，枚举类型，注解类型，和这些类型的数组

    // void show();  报错，void返回值类型不被允许
    String show1();

    int show2() default 3;  // 定义默认值，在使用注解的时候就可以不赋值了

    Person per();

    Myanno2 anno2();

    String[] show3();

    // 如果只有一个属性 而且属性的名字叫 value  在使用的时候赋值的key可以省略
    // 数组赋值的时候 用 {}包裹，当值只有一个的时候 {}可以省略
}