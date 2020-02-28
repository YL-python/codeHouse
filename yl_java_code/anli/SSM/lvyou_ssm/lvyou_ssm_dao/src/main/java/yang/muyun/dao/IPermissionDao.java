package yang.muyun.dao;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import yang.muyun.domain.Permission;

import java.util.List;

public interface IPermissionDao {

    //根据用户id查询出所有对应的角色
    @Select("select * from permission where id in (select permissionId from role_permission where roleId=#{roleId})")
    public List<Permission> findPermissionByRoleId(int roleId) throws Exception;

    @Select("select * from permission")
    List<Permission> findAll();

    @Insert("insert into permission(permissionName,url) values(#{permissionName},#{url})")
    void save(Permission permission);
}
