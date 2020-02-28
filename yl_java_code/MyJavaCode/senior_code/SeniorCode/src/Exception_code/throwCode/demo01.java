package Exception_code.throwCode;

public class demo01 {
    public static void main(String[] args) {
        int[] array = new int[3];
        //array = null;
        //int e = getElement(array, 0);
        int e = getElement(array, 3);
        System.out.println(e);

    }
    public static int getElement(int[] array, int index){
        // 写方法的第一步要对参数进行合法性检验
        if(array == null){
            throw new NullPointerException("传递的数组为空");
        }
        if(index<0 || index>array.length-1){
            throw new IndexOutOfBoundsException("越界啦");
        }
        int element = array[index];
        return element;
    }
}
