package yang.muyun.service;

import org.springframework.security.core.userdetails.UserDetailsService;
import yang.muyun.domain.RegisterData;
import yang.muyun.domain.UserInfo;
import yang.muyun.domain.UserSignIn;

public interface IUserService extends UserDetailsService {
    void register(UserInfo userInfo);

    UserInfo login(String username, String password);

    UserInfo details(String username);

    void update(UserInfo userInfo);

    Boolean findUsername(RegisterData data);
}
