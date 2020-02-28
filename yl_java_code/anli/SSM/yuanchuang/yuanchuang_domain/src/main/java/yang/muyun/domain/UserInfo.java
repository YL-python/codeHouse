package yang.muyun.domain;

import yang.muyun.utils.DateUtils;

import java.util.Date;
import java.util.List;

// 学生表
public class UserInfo {
    private Integer id;
    private String username; // 账号
    private String password; // 密码
    private String userSex; // 性别
    private String userXingMing;// 姓名
    private String grade; // 年级
    private String professional; // 专业
    private String class_; // 班级
    private String userClass;// 班级
    private String userPhoneNum;// 电话
    private Date userBirthday;// 生日
    private String userBirthdayStr;// 生日页面展示
    private List<UserSignIn> userSignInList; // 签到信息

    public String getGrade() {
        if(userClass != null){
            grade = userClass.split("-")[0];
        }
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public String getProfessional() {
        if(userClass != null){
            professional = userClass.split("-")[1];
        }
        return professional;
    }

    public void setProfessional(String professional) {
        this.professional = professional;
    }

    public String getClass_() {
        if(userClass != null){
            class_ = userClass.split("-")[2];
        }
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

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

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getUserSex() {
        return userSex;
    }

    public void setUserSex(String userSex) {
        this.userSex = userSex;
    }

    public String getUserXingMing() {
        return userXingMing;
    }

    public void setUserXingMing(String userXingMing) {
        this.userXingMing = userXingMing;
    }

    public String getUserClass() {
        if(grade == null){
            userClass = "未填写-";
        }else{
            userClass = grade + "-";
        }
        if(professional == null){
            userClass = userClass+"未填写-";
        }else{
            userClass = userClass+ professional + "-";
        }
        if(class_ == null){
            userClass = userClass+"未填写";
        }else{
            userClass = userClass+ class_;
        }
        return userClass;
    }

    public void setUserClass(String userClass) {
        this.userClass = userClass;
    }

    public String getUserPhoneNum() {
        return userPhoneNum;
    }

    public void setUserPhoneNum(String userPhoneNum) {
        this.userPhoneNum = userPhoneNum;
    }

    public Date getUserBirthday() {
        return userBirthday;
    }

    public void setUserBirthday(Date userBirthday) {
        this.userBirthday = userBirthday;
    }

    public String getUserBirthdayStr() {
        if(userBirthday != null){
            userBirthdayStr = DateUtils.date2String(userBirthday,"yyyy/MM/dd");
        }
        return userBirthdayStr;
    }

    public void setUserBirthdayStr(String userBirthdayStr) {
        this.userBirthdayStr = userBirthdayStr;
    }

    @Override
    public String toString() {
        return "UserInfo{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", userSex='" + userSex + '\'' +
                ", userXingMing='" + userXingMing + '\'' +
                ", grade='" + grade + '\'' +
                ", professional='" + professional + '\'' +
                ", class_='" + class_ + '\'' +
                ", userClass='" + userClass + '\'' +
                ", userPhoneNum='" + userPhoneNum + '\'' +
                ", userBirthday=" + userBirthday +
                ", userBirthdayStr='" + userBirthdayStr + '\'' +
                '}';
    }
}
