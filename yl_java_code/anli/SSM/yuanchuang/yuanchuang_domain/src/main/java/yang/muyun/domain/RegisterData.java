package yang.muyun.domain;

import org.springframework.security.core.parameters.P;

public class RegisterData {
    private String username;
    private Boolean flag;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Boolean getFlag() {
        return flag;
    }

    public void setFlag(Boolean flag) {
        this.flag = flag;
    }

    @Override
    public String toString() {
        return "RegisterData{" +
                "username='" + username + '\'' +
                ", flag=" + flag +
                '}';
    }
}
