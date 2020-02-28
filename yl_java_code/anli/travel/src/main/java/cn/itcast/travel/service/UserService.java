package cn.itcast.travel.service;

import cn.itcast.travel.domain.User;

public interface UserService {
    // 注册用户的方法
    boolean userRegist(User user);

    // 激活用户的方法
    boolean activeUser(String code);

    // 登录方法
    User login(User user);
}
