package main.java.web.filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.List;

@WebFilter("/*")
public class SensitiveWordsFilter implements Filter {
    private List<String> SensitiveWordsList = new ArrayList();  // 敏感词汇的集合

    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws ServletException, IOException {
        // 创建代理对象
        // 增强方法
        ServletRequest proxy_req=(ServletRequest) Proxy.newProxyInstance(req.getClass().getClassLoader(), req.getClass().getInterfaces(), new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                // 增强getParameter方法
                if(method.getName().equals("getParameter")){
                    String value = (String) method.invoke(req,args);
                    if(value != null){
                        for (String s : SensitiveWordsList) {
                            if(value.contains(s)){
                                int length = s.length();
                                String replace ="";
                                for (int i = 0; i < length; i++) {
                                    replace += "*";
                                }
                                value = value.replaceAll(s,replace);
                            }
                        }
                    }
                    return value;
                }

                //判断方法名是否是 getParameterMap


                //判断方法名是否是 getParameterValue


                return method.invoke(req,args);
            }
        });
        chain.doFilter(proxy_req, resp);
    }

    public void init(FilterConfig config) throws ServletException {
        try {
            // 加载敏感词汇.txt进内存
            // 加载文件  获取文件的真实路径
            ServletContext servletContext = config.getServletContext();
            String realPath = servletContext.getRealPath("/WEB-INF/classes/敏感词汇.txt");
            // 读取文件
            // 注意br  的编码格式 br是gbk编码 文件是U8就要设置编码
            BufferedReader br = new BufferedReader(new FileReader(realPath));
            // 文件的每一行写到数组里面
            String line = null;
            while ((line = br.readLine()) != null) {
                SensitiveWordsList.add(line);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void destroy() {
    }
}
