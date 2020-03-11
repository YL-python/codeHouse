package com.yang.bean;

public class Department {
    private Integer deptId;

    private String depyName;

    public Department() {
    }

    public Department(Integer deptId, String depyName) {
        this.deptId = deptId;
        this.depyName = depyName;
    }

    public Integer getDeptId() {
        return deptId;
    }

    public void setDeptId(Integer deptId) {
        this.deptId = deptId;
    }

    public String getDepyName() {
        return depyName;
    }

    public void setDepyName(String depyName) {
        this.depyName = depyName == null ? null : depyName.trim();
    }
}