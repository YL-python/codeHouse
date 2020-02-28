package yang.muyun.service;

import yang.muyun.domain.SysLog;

import java.util.List;

public interface ISysLogService {
    void save(SysLog sysLog);

    List<SysLog> findAll();
}
