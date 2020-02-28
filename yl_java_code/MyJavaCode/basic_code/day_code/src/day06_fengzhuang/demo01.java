package day06_fengzhuang;
/*
方法也是一种封装 把细节信息写道方法里面  外部调用方法就可以
*/
public class demo01 {
    public static void main(String[] args) {
        int[] array1 = { 1,2,3,4,100 };
        int max = GetMax(array1);
        System.out.println("最大值" + max);
    }

    // 给一个数组 返回最大值
    public static int GetMax(int[] array){
        int max = array[0];
        for(int i = 1; i < array.length; i++){
            if(array[i] > max){
                max = array[i];
            }
        }
        return max;
    }
}
