package com.yang.example2;

import java.util.Date;

public class People {
    @ylWrite
    private String name;
    private int age;
    private String tel;
    @ylWrite
    private Date birthday;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public People() {
    }

    public People(String name, int age, String tel, Date birthday) {

        this.name = name;
        this.age = age;
        this.tel = tel;
        this.birthday = birthday;
    }

    @Override
    public String toString() {
        return "People{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", tel='" + tel + '\'' +
                ", birthday=" + birthday +
                '}';
    }
}
