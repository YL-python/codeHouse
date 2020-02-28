package main.java.xml.Jsoup;

// jsoup parse方法的三种重载
// 2019年11月5日 17点08分

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.File;
import java.net.URL;

public class JsoupDemo02 {
    public static void main(String[] args) throws Exception {
        // 获取document对象 根据xml文档获取

        // 类加载器获取student.xml的path
        String xml_path = JsoupDemo02.class.getClassLoader().getResource("student.xml").getPath();
        Document document1 = Jsoup.parse(new File(xml_path), "utf-8");
        System.out.println(document1);

        String xml = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n" +
                "\n" +
                " <students>\n" +
                " \t<student number=\"heima_0001\">\n" +
                " \t\t<name>tom</name>\n" +
                " \t\t<age>18</age>\n" +
                " \t\t<sex>male</sex>\n" +
                " \t</student>\n" +
                "\n" +
                "\t<student number=\"heima_0002\">\n" +
                "\t\t<name>tom</name>\n" +
                "\t\t<age>18</age>\n" +
                "\t\t<sex>male</sex>\n" +
                "\t</student>\n" +
                " </students>";
        Document document2 = Jsoup.parse(xml);
        System.out.println(document2);

        URL url = new URL("http://fanyi.youdao.com/");
        Document document3 = Jsoup.parse(url, 1000);
        System.out.println(document3);

    }
}
