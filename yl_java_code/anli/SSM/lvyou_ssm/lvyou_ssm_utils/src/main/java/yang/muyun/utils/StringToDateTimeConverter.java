package yang.muyun.utils;

import org.springframework.core.convert.converter.Converter;
import org.springframework.stereotype.Component;

import java.util.Date;

public class StringToDateTimeConverter implements Converter<String, Date> {
    @Override
    public Date convert(String source) {
        // 判断
        if (source == null) {
            throw new RuntimeException("参数不能为空");
        }
        try {
            Date date1 = DateUtils.String2Date(source, "yyyy-MM-dd HH:mm");
            String d = DateUtils.date2String(date1,"yyyy-MM-dd HH:mm:ss");
            Date date = DateUtils.String2Date(d, "yyyy-MM-dd HH:mm:ss");
            return date;
        } catch (Exception e) {
            throw new RuntimeException("类型转换错误");
        }
    }
}
