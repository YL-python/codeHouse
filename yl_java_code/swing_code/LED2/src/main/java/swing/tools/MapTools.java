package main.java.swing.tools;

import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import main.java.swing.vo.LedDao;

public class MapTools {
	public static LedDao getLedDao(Map<String, LedDao> map,String index) {
		LedDao ledDaos = new LedDao() ;
		Set<String> keySet = map.keySet();
		for (Iterator<String> it = keySet.iterator(); it.hasNext();) {
			String key = it.next();
			try {
				if (key.equals(index)) {
					ledDaos = map.get(key);
					System.out.println("key:"+key+";value："+ledDaos);
				}
			} catch (NullPointerException e) {
				e.printStackTrace();
				System.out.println("key为null"+e.getMessage());
			}
		}
		return ledDaos ;
	}
}
