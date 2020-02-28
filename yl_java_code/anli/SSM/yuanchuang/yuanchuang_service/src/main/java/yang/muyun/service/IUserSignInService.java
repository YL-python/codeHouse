package yang.muyun.service;

import yang.muyun.domain.UserSignIn;

import java.util.List;

public interface IUserSignInService {
    void signin(UserSignIn userSignIn);

    List<UserSignIn> findAll(String username, Integer page);
}
