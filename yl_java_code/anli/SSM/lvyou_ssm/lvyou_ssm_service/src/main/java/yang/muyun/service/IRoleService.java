package yang.muyun.service;

import yang.muyun.domain.Permission;
import yang.muyun.domain.Role;

import java.util.List;

public interface IRoleService {
    List<Role> findAll();

    void save(Role role);

    Role findById(int roleId);

    List<Permission> findOtherPermissions(int roleId);

    void addPermissionToRole(int roleId, int[] permissionIds);
}
