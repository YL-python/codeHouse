package yang.muyun.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import yang.muyun.dao.IUserDao;
import yang.muyun.domain.Role;
import yang.muyun.domain.UserInfo;
import yang.muyun.service.IUserService;

import java.util.ArrayList;
import java.util.List;


@Service("userService")
@Transactional
public class UserServiceImpl implements IUserService {
    @Autowired
    private IUserDao userDao;
    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        UserInfo userInfo = userDao.findByUsername(username);

        // 把自己的用户对象封装成 UserDetails 对象
        // User user = new User(userInfo.getUsername(),"{noop}"+userInfo.getPassword(),getAuthorities(userInfo.getRoles()));
        User user = new User(userInfo.getUsername(),userInfo.getPassword(),userInfo.getStatus()==1?true:false,true,true,true, getAuthorities(userInfo.getRoles()));

        return user;
    }

    // 返回一个list集合，装有 角色的描述
    public List<SimpleGrantedAuthority> getAuthorities(List<Role> roles){
        List<SimpleGrantedAuthority> list = new ArrayList<>();
        for (Role role : roles) {
            list.add(new SimpleGrantedAuthority("ROLE_"+role.getRoleName()));
        }
        return list;
    }

    @Override
    public List<UserInfo> findAll() {
        return userDao.findAll();
    }

    @Override
    public void save(UserInfo userInfo) {
        // 密码加密
        userInfo.setPassword(bCryptPasswordEncoder.encode(userInfo.getPassword()));
        userDao.save(userInfo);
    }

    @Override
    public UserInfo findById(int id) {
        return userDao.findById(id);
    }

    @Override
    public List<Role> findOtherRole(int userId) {
        return userDao.findOtherRole(userId);
    }

    @Override
    public void addRoleToUser(int userId, int[] roleIds) {
        for (int roleId : roleIds) {
            userDao.addRoleToUser(userId,roleId);
        }
    }
}
