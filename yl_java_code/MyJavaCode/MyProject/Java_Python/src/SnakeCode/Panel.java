package SnakeCode;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;

public class Panel extends JPanel implements KeyListener, ActionListener{  // 画布类
    // 导入图片标题
    ImageIcon title = new ImageIcon("D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\SnakeCode\\images\\title.jpg");//导入图片
    ImageIcon body = new ImageIcon("D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\SnakeCode\\images\\body.png");//导入图片
    ImageIcon right = new ImageIcon("D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\SnakeCode\\images\\right.png");//导入图片
    ImageIcon left = new ImageIcon("D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\SnakeCode\\images\\left.png");//导入图片
    ImageIcon up = new ImageIcon("D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\SnakeCode\\images\\up.png");//导入图片
    ImageIcon down = new ImageIcon("D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\SnakeCode\\images\\down.png");//导入图片
    ImageIcon food = new ImageIcon("D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\SnakeCode\\images\\food.png");//导入图片

    // 蛇的数据结构  长度 每个点的坐标  蛇头方向  游戏是否开始
    int len = 3;
    int score =0;
    int[] snakeX = new int[800];
    int[] snakeY = new int[800];
    String fx = "R";
    boolean isStarted = false;
    boolean isFailed = false;
    Timer timer = new Timer(100, (ActionListener) this);  // 时钟   时间，在哪实现
    int foodx;
    int foody;
    Random rand = new Random();


    public Panel(){  // 构造方法  写初始化的内容
        initSnake();  // 初始化蛇
        this.setFocusable(true);  // 是否可以获取键盘事件
        this.addKeyListener(this);  // 添加一个时间监听者
        timer.start();  // 启动时钟
    }

    public void paintComponent(Graphics g){  // 画画函数，参数是画笔
        super.paintComponent(g);   // 调用父类方法
        this.setBackground(Color.WHITE);  // 设置背景颜色
        title.paintIcon(this, g,25,11);  // 画标题
        g.fillRect(25,75,850, 600);  //填满一个方框，起始坐标，方框大小
        g.setColor(Color.WHITE);  // 画分数
        g.drawString("len "+len,750,35);
        g.drawString("score "+score,750,50);

        // 画蛇头
        if(fx == "R"){
            right.paintIcon(this,g,snakeX[0],snakeY[0]);
        }else if(fx == "L"){
            left.paintIcon(this,g,snakeX[0],snakeY[0]);
        }else if(fx == "D"){
            down.paintIcon(this,g,snakeX[0],snakeY[0]);
        }else if(fx == "U"){
            up.paintIcon(this,g,snakeX[0],snakeY[0]);
        }
        // 画身体
        for(int i = 1;i<len;i++){
            body.paintIcon(this,g,snakeX[i],snakeY[i]);
        }
        food.paintIcon(this,g,foodx,foody);

        // 画开始提示语
        if(isStarted == false){
            g.setColor(Color.WHITE);  // 画笔颜色
            g.setFont(new Font("",Font.BOLD,40));  // 画笔字体，粗细，大小
            g.drawString("按下空格键开始游戏!",250,300);
        }
        if(isFailed){
            g.setColor(Color.red);  // 画笔颜色
            g.setFont(new Font("",Font.BOLD,40));  // 画笔字体，粗细，大小
            g.drawString("游戏结束",250,300);
            g.drawString("按下空格键重新开始游戏!",250,350);
        }

    }

    public void initSnake(){
        len = 3;
        score = 0;
        snakeX[0] = 100;
        snakeY[0] = 100;
        snakeX[1] = 75;
        snakeY[1] = 100;
        snakeX[2] = 50;
        snakeY[2] = 100;
        fx = "R";
        foodx = 25 + 25 * rand.nextInt(34);
        foody = 75 + 25 * rand.nextInt(24);
    }

    @Override
    public void keyTyped(KeyEvent e) {  // 敲键
    }

    @Override
    public void keyPressed(KeyEvent e) {  // 敲到底
        // KeyEvent 参数是键  每个键对应一个数字
        int keyCode = e.getKeyCode();
        if(keyCode == KeyEvent.VK_SPACE){
            if(isFailed){
                isFailed = false;
                initSnake();
            }else{
                isStarted = !isStarted;
            }
            repaint();  // 重新画  函数
        }
        if((keyCode == KeyEvent.VK_DOWN) && fx != "U"){
            fx = "D";
            repaint();
        }
        if((keyCode == KeyEvent.VK_RIGHT) && fx != "L"){
            fx = "R";
            repaint();
        }
        if((keyCode == KeyEvent.VK_LEFT) && fx != "R"){
            fx = "L";
            repaint();
        }
        if((keyCode == KeyEvent.VK_UP) && fx != "D"){
            fx = "U";
            repaint();
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {  // 松开
    }

    @Override
    public void actionPerformed(ActionEvent e) {  // 时间到了就会调用这个方法
        // 移动身体
        if(isStarted && !isFailed){  // 暂停
            for(int i = len-1; i>0;i--){
                snakeX[i] = snakeX[i-1];
                snakeY[i] = snakeY[i-1];
            }
            if(fx == "R"){
                snakeX[0] = snakeX[0] + 25;
                if(snakeX[0]>850)snakeX[0]=25;
            }else if(fx == "L"){
                snakeX[0] = snakeX[0] - 25;
                if(snakeX[0]<25)snakeX[0]=850;
            }else if(fx == "D"){
                snakeY[0] = snakeY[0] + 25;
                if(snakeY[0]>650)snakeY[0]=75;
            }else if(fx == "U"){
                snakeY[0] = snakeY[0] - 25;
                if(snakeY[0]<75)snakeY[0]=650;
            }

            if(snakeX[0] == foodx && snakeY[0] == foody){  // 长度增加
                len++;
                score = score + 10;
                foodx = 25 + 25 * rand.nextInt(34);
                foody = 75 + 25 * rand.nextInt(24);
            }

            for(int i=1;i<len;i++){
                if(snakeX[i] == snakeX[0] && snakeY[i] == snakeY[0]){  // 碰撞死亡
                    isFailed = !isFailed;
                }
            }

            repaint();
        }

        timer.start();  // 启动时钟
    }
}
