package yang.muyun.dao.impl;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import yang.muyun.dao.UserDao;
import yang.muyun.domain.User;

import java.util.List;

public class UserDaoImpl implements UserDao {

    private SqlSessionFactory factory;

    public UserDaoImpl(SqlSessionFactory factory){
        this.factory = factory;
    }

    public List<User> findAll() {
        // 根据factory 获取sqlsession对象
        SqlSession sqlSession = factory.openSession();
        // SqlSession 方法查询列表
        // 参数是能获取信息的 key
        List<User> users = sqlSession.selectList("yang.muyun.dao.UserDao.findAll");
        // 释放资源
        sqlSession.close();
        return users;
    }

    public void saveUser(User user) {
        // 根据factory 获取sqlsession对象
        SqlSession sqlSession = factory.openSession();
        sqlSession.insert("yang.muyun.dao.UserDao.saveUser",user);
        // 提交事务
        sqlSession.commit();
        sqlSession.close();
    }

    public void updateUser(User user) {
        // 根据factory 获取sqlsession对象
        SqlSession sqlSession = factory.openSession();
        sqlSession.update("yang.muyun.dao.UserDao.updateUser",user);
        // 提交事务
        sqlSession.commit();
        sqlSession.close();
    }

    public void deleteUser(Integer userId) {
        // 根据factory 获取sqlsession对象
        SqlSession sqlSession = factory.openSession();
        sqlSession.delete("yang.muyun.dao.UserDao.deleteUser",userId);
        // 提交事务
        sqlSession.commit();
        sqlSession.close();
    }

    public User findById(Integer userId) {
        // 根据factory 获取sqlsession对象
        SqlSession sqlSession = factory.openSession();
        // SqlSession 方法查询列表
        // 参数是能获取信息的 key
        User user = sqlSession.selectOne("yang.muyun.dao.UserDao.findById",userId);
        // 释放资源
        sqlSession.close();
        return user;
    }

    public List<User> findByName(String username) {
        // 根据factory 获取sqlsession对象
        SqlSession sqlSession = factory.openSession();
        // SqlSession 方法查询列表
        // 参数是能获取信息的 key
        List<User> users = sqlSession.selectOne("yang.muyun.dao.UserDao.findByName",username);
        // 释放资源
        sqlSession.close();
        return users;
    }

    public int findTotal() {
        // 根据factory 获取sqlsession对象
        SqlSession sqlSession = factory.openSession();
        // SqlSession 方法查询列表
        // 参数是能获取信息的 key
        Integer count = sqlSession.selectOne("yang.muyun.dao.UserDao.findTotal");
        // 释放资源
        sqlSession.close();
        return count;
    }
}
