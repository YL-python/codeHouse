package Map_code;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class demo_entry {
    public static void main(String[] args) {
        Map<String,Integer> map = new HashMap<>();
        map.put("yang",10);
        map.put("long",11);
        map.put("huan",15);
        Set<Map.Entry<String, Integer>> set = map.entrySet();
        Iterator<Map.Entry<String, Integer>> it = set.iterator();
        while(it.hasNext()) {
            Map.Entry<String, Integer> entry = it.next();
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println("key="+ key+";value="+value);
        }
        System.out.println("------------------------");
        for (Map.Entry<String, Integer> entry :set){
            System.out.println(entry.getKey());
            System.out.println(entry.getValue());
        }
    }
}
