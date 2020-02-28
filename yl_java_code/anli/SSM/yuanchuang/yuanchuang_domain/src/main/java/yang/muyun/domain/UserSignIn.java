package yang.muyun.domain;

import yang.muyun.utils.DateUtils;

import java.text.ParseException;
import java.util.Date;

/*
UserSignIn{
id=null,
qdMood='无聊',
qdDate=null,
qdDateStr='2020/02/06',
qdStartTime=null,
qdStartTimehh='11',
qdStartTimemm='10',
qdEndTime=null,
qdEndTimehh='16',
qdEndTimemm='10',
qdStudyTime=null,
qdTodayContent='做签到页面',
qdTomorrowContent='继续做签到页面',
qdUsername='tom'}
*/

public class UserSignIn {
    private Integer id;  // 签到 id
    private String qdMood; // 签到心情
    private Date qdDate; // 签到日期 yyyy/MM/dd
    private String qdDateStr; // 签到日期 页面提交的字符串 yyyy/MM/dd

    private Date qdStartTime; // 签到开始时间 hh:mm
    private String qdStartTimehh; // 签到开始时间 页面提交的字符串 hh
    private String qdStartTimemm;// 签到开始时间 页面提交的字符串 mm

    private Date qdEndTime; // 签到结束时间 hh:mm
    private String qdEndTimehh; // 签到结束时间 页面提交的字符串 hh
    private String qdEndTimemm;// 签到结束时间 页面提交的字符串 mm

    private Date qdStudyTime; // 签到 学习时间 结束时间- 开始时间
    private String qdStudyTimeStr; // 学习时间 字符串表示

    private String qdTodayContent; // 签到今天学习内容
    private String qdTomorrowContent; // 签到明天学习内容
    private String qdUsername; // 签到用户名

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getQdMood() {
        return qdMood;
    }

    public void setQdMood(String qdMood) {
        this.qdMood = qdMood;
    }

    public Date getQdDate() throws ParseException {
        if (qdDateStr != null){
            qdDate = DateUtils.String2Date(qdDateStr,"yyyy/MM/dd");
        }
        return qdDate;
    }

    public void setQdDate(Date qdDate) {
        this.qdDate = qdDate;
    }

    public String getQdDateStr() {
        if(qdDate != null){
            qdDateStr = DateUtils.date2String(qdDate,"yyyy年MM月dd日");
        }
        return qdDateStr;
    }

    public void setQdDateStr(String qdDateStr) {
        this.qdDateStr = qdDateStr;
    }

    public Date getQdStartTime() throws ParseException {
        if(qdStartTimehh != null && qdStartTimemm != null){
            String qdStartTimeStr = qdStartTimehh + ":" + qdStartTimemm;
            qdStartTime = DateUtils.String2Date(qdStartTimeStr,"HH:mm");
        }
        return qdStartTime;
    }

    public void setQdStartTime(Date qdStartTime) {
        this.qdStartTime = qdStartTime;
    }

    public String getQdStartTimehh() {
        return qdStartTimehh;
    }

    public void setQdStartTimehh(String qdStartTimehh) {
        this.qdStartTimehh = qdStartTimehh;
    }

    public String getQdStartTimemm() {
        return qdStartTimemm;
    }

    public void setQdStartTimemm(String qdStartTimemm) {
        this.qdStartTimemm = qdStartTimemm;
    }

    public Date getQdEndTime() throws ParseException {
        if(qdEndTimehh != null && qdEndTimemm != null){
            String qdEndTimeStr = qdEndTimehh + ":" + qdEndTimemm;
            qdEndTime = DateUtils.String2Date(qdEndTimeStr,"HH:mm");
        }
        return qdEndTime;
    }

    public void setQdEndTime(Date qdEndTime) {
        this.qdEndTime = qdEndTime;
    }

    public String getQdEndTimehh() {
        return qdEndTimehh;
    }

    public void setQdEndTimehh(String qdEndTimehh) {
        this.qdEndTimehh = qdEndTimehh;
    }

    public String getQdEndTimemm() {
        return qdEndTimemm;
    }

    public void setQdEndTimemm(String qdEndTimemm) {
        this.qdEndTimemm = qdEndTimemm;
    }

    public Date getQdStudyTime() throws ParseException {
        Date endTime = getQdEndTime();
        Date startTime = getQdStartTime();
        qdStudyTime = DateUtils.sub(endTime,startTime);
        return qdStudyTime;
    }

    public void setQdStudyTime(Date qdStudyTime) {
        this.qdStudyTime = qdStudyTime;
    }

    public String getQdStudyTimeStr() {
        if (qdStudyTime != null){
            qdStudyTimeStr = DateUtils.date2String(qdStudyTime,"HH小时mm分");
        }
        return qdStudyTimeStr;
    }

    public void setQdStudyTimeStr(String qdStudyTimeStr) {
        this.qdStudyTimeStr = qdStudyTimeStr;
    }

    public String getQdTodayContent() {
        return qdTodayContent;
    }

    public void setQdTodayContent(String qdTodayContent) {
        this.qdTodayContent = qdTodayContent;
    }

    public String getQdTomorrowContent() {
        return qdTomorrowContent;
    }

    public void setQdTomorrowContent(String qdTomorrowContent) {
        this.qdTomorrowContent = qdTomorrowContent;
    }

    public String getQdUsername() {
        return qdUsername;
    }

    public void setQdUsername(String qdUsername) {
        this.qdUsername = qdUsername;
    }

    @Override
    public String toString() {
        return "UserSignIn{" +
                "id=" + id +
                ", qdMood='" + qdMood + '\'' +
                ", qdDate=" + qdDate +
                ", qdDateStr='" + qdDateStr + '\'' +
                ", qdStartTime=" + qdStartTime +
                ", qdStartTimehh='" + qdStartTimehh + '\'' +
                ", qdStartTimemm='" + qdStartTimemm + '\'' +
                ", qdEndTime=" + qdEndTime +
                ", qdEndTimehh='" + qdEndTimehh + '\'' +
                ", qdEndTimemm='" + qdEndTimemm + '\'' +
                ", qdStudyTime=" + qdStudyTime +
                ", qdTodayContent='" + qdTodayContent + '\'' +
                ", qdTomorrowContent='" + qdTomorrowContent + '\'' +
                ", qdUsername='" + qdUsername + '\'' +
                '}';
    }

}
