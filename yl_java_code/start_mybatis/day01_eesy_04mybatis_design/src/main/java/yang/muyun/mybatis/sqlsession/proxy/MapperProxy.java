package yang.muyun.mybatis.sqlsession.proxy;

import yang.muyun.mybatis.cfg.Mapper;
import yang.muyun.mybatis.utils.Executor;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.sql.Connection;
import java.util.Map;

public class MapperProxy implements InvocationHandler {

    // mappers 的key是全限定类名+方法名和 SQL语句
    private Map<String,Mapper> mappers;
    private Connection conn;

    public MapperProxy(Map<String, Mapper> mappers, Connection conn) {
        this.mappers = mappers;
        this.conn = conn;
    }

    // 用于增强方法  我们的增强就是调用 selectList方法
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 获取方法名
        String methodName = method.getName();
        // 获取方法所在类的名称
        String className = method.getDeclaringClass().getName();
        // 组合key
        String key = className + "." + methodName;
        // 获取mappers中的Mapper对象
        Mapper mapper = mappers.get(key);
        // 判断有没有结果
        if(mapper == null ){
            throw new IllegalArgumentException("传入的参数有误");
        }
        // 调用工具类执行查询语句 获得结果集
        return new Executor().selectList(mapper,conn);
    }
}
