package cn.itcast.travel.service.impl;

import cn.itcast.travel.dao.UserDao;
import cn.itcast.travel.dao.impl.UserDaoImpl;
import cn.itcast.travel.domain.User;
import cn.itcast.travel.service.UserService;
import cn.itcast.travel.util.MailUtils;
import cn.itcast.travel.util.UuidUtil;

public class UserServiceImpl implements UserService {

    private UserDao userDao = new UserDaoImpl();
    // 注册用户的方法
    @Override
    public boolean userRegist(User user) {
        // 根据用户名查询用户对象
        User userByName = userDao.findUserByName(user.getUsername());
        if(userByName == null){
            // 注册成功
            // 设置激活状态
            user.setStatus("N");
            // 设置激活码
            user.setCode(UuidUtil.getUuid());
            // 保存用户信息
            userDao.saveUser(user);
            // 发送激活邮件
            String content = "<a href='http://localhost/travel/user/active?code="+user.getCode()+"'>点击激活【黑马旅游网】</a>";
            MailUtils.sendMail(user.getEmail(),content,"激活邮件");
            return true;
        }else {
            // 用户名存在，注册失败
            return false;
        }
    }

    // 激活用户的方法
    @Override
    public boolean activeUser(String code) {
        // 根据激活码查询对象
        User user = userDao.findUserByCode(code);
        if(user != null){
            // 设置激活状态
            userDao.updateStatus(user);
            return true;
        }else {
            return false;
        }
    }

    // 登录方法
    @Override
    public User login(User user) {
        User u =  userDao.findUserByNAndP(user);
        return u;
    }
}
