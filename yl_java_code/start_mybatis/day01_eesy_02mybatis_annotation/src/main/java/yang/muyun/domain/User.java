package yang.muyun.domain;

import java.io.Serializable;
import java.util.Date;

/*
Serializable接口是启用其序列化功能的接口。
实现java.io.Serializable 接口的类是可序列化的。
没有实现此接口的类将不能使它们的任意状态被序列化或逆序列化。
Serializable接口是一个里面什么都没有的接口
这个接口是一个标识接口
告诉JVM此类可被序列化，可被默认的序列化机制序列化。
*/

public class User implements Serializable {
    private Integer id;
    private String username;
    private Date birthday;
    private String sex;
    private String address;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", birthday=" + birthday +
                ", sex='" + sex + '\'' +
                ", address='" + address + '\'' +
                '}';
    }

}
