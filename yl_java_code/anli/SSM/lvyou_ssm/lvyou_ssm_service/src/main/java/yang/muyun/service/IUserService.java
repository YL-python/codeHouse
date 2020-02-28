package yang.muyun.service;

import org.springframework.security.core.userdetails.UserDetailsService;
import yang.muyun.domain.Role;
import yang.muyun.domain.UserInfo;

import java.util.List;

public interface IUserService extends UserDetailsService {

    List<UserInfo> findAll();

    void save(UserInfo userInfo);

    UserInfo findById(int id);

    List<Role> findOtherRole(int userId);

    void addRoleToUser(int userId, int[] roleIds);
}
