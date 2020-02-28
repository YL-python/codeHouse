package day04_array;

public class Array_Max {
    public static void main(String[] args) {
        int[] array1 = { 1, 2, 3, 4, 5 };
        int array_max = array1[0];
        int array_len = array1.length;

        for(int i = 1; i < array_len; i++){
            if(array1[i] > array_max){
                array_max = array1[i];
            }
        }

        System.out.println(array_max);

    }
}
