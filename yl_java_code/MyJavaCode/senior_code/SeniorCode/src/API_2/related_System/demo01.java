package API_2.related_System;

import java.util.Arrays;

public class demo01 {
    public static void main(String[] args) {
        System.out.println(System.currentTimeMillis());  // 获取时间戳
        int[] array1 = { 1, 2, 3, 4 };
        int[] array2 = new int[4];
        System.arraycopy(array1,0,array2,0,array1.length);
        System.out.println(Arrays.toString(array2));
    }
}
