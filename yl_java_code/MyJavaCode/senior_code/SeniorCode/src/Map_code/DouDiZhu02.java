package Map_code;

import java.util.*;

public class DouDiZhu02 {
    public static void main(String[] args) {
        String[] colors = { "♠", "♥", "♣", "♦" };
        String[] numbers = { "2", "1", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3"};
        ArrayList<String> poker = new ArrayList<>();
        ArrayList<Integer> pokerIndex = new ArrayList<>();
        poker.add("大王");
        poker.add("小王");
        for (String number : numbers) {
            for (String color : colors) {
                poker.add(color+number);
            }
        }
        HashMap<Integer, String> pokerMap = new HashMap<>();
        for(Integer i=0;i<poker.size();i++){
            pokerMap.put(i,poker.get(i));
            pokerIndex.add(i);
        }

        Collections.shuffle(pokerIndex);
        ArrayList<Integer> dipai = new ArrayList<>();
        ArrayList<Integer> player00 = new ArrayList<>();
        ArrayList<Integer> player01 = new ArrayList<>();
        ArrayList<Integer> player02 = new ArrayList<>();
        for (int i = 0; i < pokerIndex.size(); i++) {
            if (i >= 51){
                dipai.add(pokerIndex.get(i));
            }else if(i%3 == 0){
                player00.add(pokerIndex.get(i));
            }else if(i%3 == 1){
                player01.add(pokerIndex.get(i));
            }else if(i%3 == 2){
                player02.add(pokerIndex.get(i));
            }
        }

        Collections.sort(player00);
        Collections.sort(player01);
        Collections.sort(player02);
        Collections.sort(dipai);
        // 看牌
        lookPoker("玩家1", player00, pokerMap);
        lookPoker("玩家2", player01, pokerMap);
        lookPoker("玩家3", player02, pokerMap);
        lookPoker("底牌 ", dipai, pokerMap);
    }
    public static void lookPoker(String name, ArrayList<Integer> list, HashMap<Integer, String> map){
        System.out.print(name + ": ");
        for (Integer key : list) {
            String s = map.get(key);
            System.out.print(s + " ");
        }
        System.out.println();
    }
}
