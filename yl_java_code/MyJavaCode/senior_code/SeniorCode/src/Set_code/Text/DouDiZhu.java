package Set_code.Text;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class DouDiZhu {
    public static void main(String[] args) {
        ArrayList<String> poker = new ArrayList<>();
        String[] colors = { "♠", "♣", "♦", "♥" };
        String[] numbers = { "2", "1", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
        poker.add("大王");
        poker.add("小王");
        for (String color : colors) {
            for (String number : numbers) {
                poker.add(color+number);
            }
        }

        Collections.shuffle(poker);
//        System.out.println(poker);
        ArrayList<String> dipai = new ArrayList<>();
        ArrayList<String> player00 = new ArrayList<>();
        ArrayList<String> player01 = new ArrayList<>();
        ArrayList<String> player02 = new ArrayList<>();
        for (int i = 0; i < poker.size(); i++) {
            if (i >= 51){
                dipai.add(poker.get(i));
            }else if(i%3 == 0){
                player00.add(poker.get(i));
            }else if(i%3 == 1){
                player01.add(poker.get(i));
            }else if(i%3 == 2){
                player02.add(poker.get(i));
            }
        }
        System.out.println("底牌是：" + dipai.toString());
        System.out.println("玩家1的手牌是：" + player00.toString());
        System.out.println("玩家2的手牌是：" + player01.toString());
        System.out.println("玩家3的手牌是：" + player02.toString());
    }

}
