package yang.muyun.test;

import org.junit.Test;
import yang.muyun.utils.DateUtils;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class dateTest {
    @Test
    public void test1() throws ParseException {
        Date startDate = DateUtils.String2Date("08:53", "HH:mm");
        Date endDate = DateUtils.String2Date("09:57", "HH:mm");
        System.out.println(startDate.getTime());
        System.out.println(endDate.getTime());
        System.out.println(DateUtils.date2String(new Date(endDate.getTime() - startDate.getTime() - 8 * 3600 * 1000),"HH:mm"));
        System.out.println(new Date(7020000));

    }
}
