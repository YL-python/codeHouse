package Map_code;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class text01 {
    public static void main(String[] args) {
        System.out.print("请输入一个字符串：");
        String input_str = new Scanner(System.in).next();
        char[] input_list = input_str.toCharArray();
        Map<Character, Integer> map = new HashMap<>();
        for (char c : input_list) {
            if(map.containsKey(c)){
                Integer count = map.get(c) + 1;
                map.put(c,count);
            }else{
                map.put(c,1);
            }
        }
        Set<Map.Entry<Character, Integer>> entries = map.entrySet();
        for (Map.Entry<Character, Integer> entry : entries) {
            System.out.println(entry.getKey() + "出现了" + entry.getValue() + "次");
        }

    }
}
