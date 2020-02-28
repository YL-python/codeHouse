package yang.muyun.dao;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Service;
import yang.muyun.domain.UserSignIn;

import java.util.List;

public interface IUserSignInDao {

    // 添加一条签到信息
    @Insert("insert into qd(qdMood,qdDate,qdStartTime,qdEndTime,qdStudyTime,qdTodayContent,qdTomorrowContent,qdUsername) " +
            "values(#{qdMood},#{qdDate},#{qdStartTime},#{qdEndTime},#{qdStudyTime},#{qdTodayContent},#{qdTomorrowContent},#{qdUsername})")
    void addUserSignIn(UserSignIn userSignIn);

    @Select("select * from qd where qdUsername=#{username} order by id desc")
    List<UserSignIn> findAll(String username);
}
