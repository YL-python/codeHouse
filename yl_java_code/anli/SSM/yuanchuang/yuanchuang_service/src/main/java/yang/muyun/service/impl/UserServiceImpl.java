package yang.muyun.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import yang.muyun.dao.IUserDao;
import yang.muyun.domain.RegisterData;
import yang.muyun.domain.UserInfo;
import yang.muyun.domain.UserSignIn;
import yang.muyun.service.IUserService;

import java.util.ArrayList;
import java.util.List;

@Service("userService")
@Transactional
public class UserServiceImpl implements IUserService {

    @Autowired
    IUserDao userDao;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        UserInfo userInfo = userDao.findByUsername(username);
        User user = new User(userInfo.getUsername(),"{noop}"+userInfo.getPassword(),getAuthorities());
        return user;
    }
    // 返回一个list集合，装有 角色的描述
    public List<SimpleGrantedAuthority> getAuthorities(){
        List<SimpleGrantedAuthority> list = new ArrayList<>();
        list.add(new SimpleGrantedAuthority("ROLE_STUDENT"));
        return list;
    }

    // 注册方法，获取一个学生对象添加到数据库中
    @Override
    public void register(UserInfo userInfo) {
        System.out.println(userInfo);
        userDao.save(userInfo);
    }

    // 登录方法，通过账户和密码查找用户，返回改用户是否存在
    @Override
    public UserInfo login(String username, String password) {
        return userDao.findStudentByUsernameAndPassword(username,password);
    }

    // 查看用户详情方法
    @Override
    public UserInfo details(String username) {
        return userDao.findByUsername(username);
    }

    // 修改用户信息
    @Override
    public void update(UserInfo userInfo) {
        userDao.updateByUsername(userInfo);
    }

    @Override
    public Boolean findUsername(RegisterData data) {
        Integer count = userDao.findUsername(data);
        if (count == 0){
            // 不存在用户返回false
            return false;
        }else{
            return true;
        }
    }

}
