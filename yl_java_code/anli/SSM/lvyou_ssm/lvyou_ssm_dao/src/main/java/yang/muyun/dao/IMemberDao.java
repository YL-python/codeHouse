package yang.muyun.dao;

import org.apache.ibatis.annotations.Select;
import yang.muyun.domain.Member;

public interface IMemberDao {
    // 根据id查询
    @Select("select * from member where id=#{id}")
    public Member findById(int id);
}
