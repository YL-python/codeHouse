package yang.muyun.test;

import org.junit.Test;
import yang.muyun.utils.DateUtils;

import java.text.ParseException;
import java.util.Date;

public class datetest {
    @Test
    public void time222() throws ParseException {
        String date = "2020-01-01 12:20";
        Date date1 = DateUtils.String2Date(date, "yyyy-MM-dd HH:mm");
        System.out.println(date1);
        System.out.println("----------------");
        String d = DateUtils.date2String(date1,"yyyy-MM-dd HH:mm:ss");
        System.out.println(d);
        System.out.println("----------------");
        System.out.println(DateUtils.String2Date(d,"yyyy-MM-dd HH:mm:ss"));
    }
}
