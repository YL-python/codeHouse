package day04_array;

public class array_retuen {

    public static void main(String[] args) {
        int[] array_1 = { 10, 20, 30 };
        int[] result = arrat_method(array_1);
        System.out.println("和：" + result[0]);
        System.out.println("平均数：" + result[1]);
    }

    public static int[] arrat_method(int[] array){
        int len = array.length;
        int sum = 0;
        for(int i = 0; i < len; i++){
            sum += array[i];
        }
        int[] result = { sum, sum/len };
        return result;
    }
}
