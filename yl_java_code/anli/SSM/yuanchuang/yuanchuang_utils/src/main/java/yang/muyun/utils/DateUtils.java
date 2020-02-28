package yang.muyun.utils;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateUtils {
    // 日期转字符串
    public static String date2String(Date date, String patt){
        SimpleDateFormat sdf = new SimpleDateFormat(patt);
        String format = sdf.format(date);
        return format;
    }

    // 字符串转日期
    public static Date String2Date(String str, String patt) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat(patt);
        Date parse = sdf.parse(str);
        return parse;
    }

    // 时间相减
    public static Date sub(Date endTime, Date startTime){
        return new Date(endTime.getTime() - startTime.getTime() - 8 * 3600 * 1000);
    }
}
