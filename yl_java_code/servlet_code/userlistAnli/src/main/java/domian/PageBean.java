package main.java.domian;

import java.util.List;

/*
分析：
客户端需要（输出）：一共有多少数据，一共有多少页，当前页的数据，当前的页码
服务器端需要（输入）：我们规定了一页多少数据，当前的页码
定义一个对象来封装数据，最后来呈现
 */

public class PageBean<T> {  // 自定义泛型，之后通用性更强
    private int totalCount;  // 用来记录数据库的总数据
    private int totalPage;  // 用来记录一共有多少页的
    private List<T> userList;  // 用来装当前页的数据
    private int currentPage;  // 当前的页码
    private final int rows = 5;  // 表示每一页多少数据

    public int getTotalCount() {
        return totalCount;
    }

    public void setTotalCount(int totalCount) {
        this.totalCount = totalCount;
    }

    public int getTotalPage() {
        return totalPage;
    }

    public void setTotalPage(int totalPage) {
        this.totalPage = totalPage;
    }

    public List<T> getUserList() {
        return userList;
    }

    public void setUserList(List<T> userList) {
        this.userList = userList;
    }

    public int getCurrentPage() {
        return currentPage;
    }

    public void setCurrentPage(int currentPage) {
        this.currentPage = currentPage;
    }

    public int getRows() {
        return rows;
    }

    @Override
    public String toString() {
        return "PageBean{" +
                "totalCount=" + totalCount +
                ", totalPage=" + totalPage +
                ", userList=" + userList +
                ", currentPage=" + currentPage +
                ", rows=" + rows +
                '}';
    }
}
