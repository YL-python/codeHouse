package cn.itcast.travel.dao;

import cn.itcast.travel.domain.User;

public interface UserDao {
    // 根据用户名查询用户信息
    public User findUserByName(String username);

    // 保存用户信息
    public void saveUser(User user);

    // 通过激活码查找用户
    User findUserByCode(String code);

    // 设置用户激活状态
    void updateStatus(User user);

    // 按用户名和密码查找用户
    User findUserByNAndP(User user);
}
