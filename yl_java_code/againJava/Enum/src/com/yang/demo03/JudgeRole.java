package com.yang.demo03;

public class JudgeRole {
    public static void main(String[] args) {
        String judge = judge(RoleEnum.ROLE_NORMAL.toString());
        System.out.println(judge);
    }

    public static String judge(String roleName) {
        // 一行代码搞定！之前的if/else灰飞烟灭
        return RoleEnum.valueOf(roleName).op();
    }
}
