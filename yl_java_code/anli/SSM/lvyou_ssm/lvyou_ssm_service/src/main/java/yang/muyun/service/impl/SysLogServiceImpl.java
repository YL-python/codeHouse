package yang.muyun.service.impl;

import org.aspectj.lang.annotation.After;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import yang.muyun.dao.ISysLogDao;
import yang.muyun.domain.SysLog;
import yang.muyun.service.ISysLogService;

import java.util.List;

@Service
@Transactional  // 事务注解
public class SysLogServiceImpl implements ISysLogService {

    @Autowired
    private ISysLogDao sysLogDao;

    @Override
    public void save(SysLog sysLog) {
        sysLogDao.save(sysLog);
    }

    @Override
    public List<SysLog> findAll() {
        return sysLogDao.findAll();
    }
}
