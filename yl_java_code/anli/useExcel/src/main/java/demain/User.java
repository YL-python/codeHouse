package main.java.demain;

public class User {
    private int id;
    private String name;
    private String tel;
    private String teacher_home;
    private int count;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getTeacher_home() {
        return teacher_home;
    }

    public void setTeacher_home(String teacher_home) {
        this.teacher_home = teacher_home;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    @Override
    public String toString() {
        return "user{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", tel='" + tel + '\'' +
                ", teacher_home='" + teacher_home + '\'' +
                ", count=" + count +
                '}';
    }
}
