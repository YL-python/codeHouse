package main.java.demain;

public class Test {
    private String username;
    private String password;

    public Test(String username, String password) {
        this.username = username;
        this.password = password;
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

    @Override
    public String toString() {
        return "Test{" +
                "username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
