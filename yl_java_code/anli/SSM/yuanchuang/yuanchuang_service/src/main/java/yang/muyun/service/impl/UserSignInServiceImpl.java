package yang.muyun.service.impl;

import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import yang.muyun.dao.IUserSignInDao;
import yang.muyun.domain.UserSignIn;
import yang.muyun.service.IUserSignInService;

import java.util.List;

@Service
@Transactional
public class UserSignInServiceImpl implements IUserSignInService {

    @Autowired
    IUserSignInDao userSignInDao;

    @Override
    public void signin(UserSignIn userSignIn) {
        userSignInDao.addUserSignIn(userSignIn);
    }

    @Override
    public List<UserSignIn> findAll(String username, Integer page) {
        PageHelper.startPage(page,10);
        return userSignInDao.findAll(username);
    }
}
