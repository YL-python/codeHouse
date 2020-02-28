package yang.muyun.mybatis.sqlsession;

// 打开一个SqlSession对象
public interface SqlSessionFactory {
    SqlSession openSession();
}
