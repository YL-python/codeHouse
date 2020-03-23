package com.yang.demo01;

public class demo01 {
    public static void main(String[] args) {
        com.yang.demo.UserRole role1 = com.yang.demo.UserRole.ROLE_ROOT_ADMIN;
        com.yang.demo.UserRole role2 = com.yang.demo.UserRole.ROLE_ORDER_ADMIN;
        com.yang.demo.UserRole role3 = com.yang.demo.UserRole.ROLE_NORMAL;

        // values()方法：返回所有枚举常量的数组集合
        for (com.yang.demo.UserRole role : com.yang.demo.UserRole.values()) {
            System.out.println(role);
        }

        // ordinal()方法：返回枚举常量的序数，注意从0开始
        System.out.println(role1.ordinal()); // 打印0
        System.out.println(role2.ordinal()); // 打印1
        System.out.println(role3.ordinal()); // 打印2

        // compareTo()方法：枚举常量间的比较
        System.out.println(role1.compareTo(role2)); //打印-1
        System.out.println(role2.compareTo(role3)); //打印-2
        System.out.println(role1.compareTo(role3)); //打印-2

        // name()方法：获得枚举常量的名称
        System.out.println(role1.name()); // 打印ROLE_ROOT_ADMIN
        System.out.println(role2.name()); // 打印ROLE_ORDER_ADMIN
        System.out.println(role3.name()); // 打印ROLE_NORMAL

        // valueOf()方法：返回指定名称的枚举常量
        System.out.println(com.yang.demo.UserRole.valueOf("ROLE_ROOT_ADMIN"));
        System.out.println(com.yang.demo.UserRole.valueOf("ROLE_ORDER_ADMIN"));
        System.out.println(com.yang.demo.UserRole.valueOf("ROLE_NORMAL"));

        com.yang.demo.UserRole userRole = com.yang.demo.UserRole.ROLE_ORDER_ADMIN;
        switch (userRole) {
            case ROLE_ROOT_ADMIN:  // 比如此处的意义就非常清晰了，比1，2，3这种数字好！
                System.out.println("这是系统管理员角色");
                break;
            case ROLE_ORDER_ADMIN:
                System.out.println("这是订单管理员角色");
                break;
            case ROLE_NORMAL:
                System.out.println("这是普通用户角色");
                break;
        }
    }
}
