package main.java.xml.Jsoup;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;

public class JsoupDemo01 {
    public static void main(String[] args) throws Exception {
        // 获取document对象 根据xml文档获取

        // 类加载器获取student.xml的path
        String xml_path = JsoupDemo01.class.getClassLoader().getResource("student.xml").getPath();

        // 解析xml文件进内存获取dom树--->document对象
        Document document = Jsoup.parse(new File(xml_path), "utf-8");

        // 获取元素对象  想想JS里面的document
        Elements elements = document.getElementsByTag("name");
        System.out.println(elements.size());

        // 获取第一个element对象
        Element element = elements.get(0);

        // 获取数据
        String text = element.text();
        System.out.println(text);

    }
}
