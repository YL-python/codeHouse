package main.java.xml.Jsoup;

// jsoup xpath 方法获取元素
// 2019年11月5日 17点42分

import cn.wanghaomiao.xpath.model.JXDocument;
import cn.wanghaomiao.xpath.model.JXNode;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.File;
import java.util.List;

public class JsoupDemo03 {
    public static void main(String[] args) throws Exception {
        // 类加载器获取student.xml的path
        String xml_path = JsoupDemo03.class.getClassLoader().getResource("student.xml").getPath();
        Document document1 = Jsoup.parse(new File(xml_path), "utf-8");
        // 把document对象变成 JXdocument对象
        JXDocument jxDocument = new JXDocument(document1);

        // 结合xpath语法查询
        List<JXNode> sel = jxDocument.selN("//student[@number='heima_0001']/name");
        for (JXNode jxNode : sel) {
            System.out.println(jxNode.getElement().text());
        }

    }
}
