package yang.muyun.controller;

import com.sun.org.apache.xpath.internal.operations.Bool;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextImpl;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;
import yang.muyun.domain.RegisterData;
import yang.muyun.domain.UserInfo;
import yang.muyun.service.IUserService;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

@Controller
@RequestMapping("/user")
public class UserController {

    @Autowired
    IUserService userService;

    @RequestMapping("/register")
    public ModelAndView register(UserInfo userInfo) {
        ModelAndView mv = new ModelAndView();
        userService.register(userInfo);
        mv.addObject("user", userInfo);
        mv.setViewName("register-200");
        return mv;
    }

    @RequestMapping("/login")
    public ModelAndView login(String username, String password) {
        ModelAndView mv = new ModelAndView();
        UserInfo userInfo = userService.login(username, password);
        if (userInfo == null) {
            mv.setViewName("login-500");
        } else {
            mv.addObject("user", userInfo);
            mv.setViewName("main");
        }
        return mv;
    }

    // 个人信息管理
    @RequestMapping("/details")
    public ModelAndView details(HttpServletRequest request) {
        ModelAndView mv = new ModelAndView();
        SecurityContextImpl securityContextImpl = (SecurityContextImpl) request.getSession().getAttribute("SPRING_SECURITY_CONTEXT");
        String username = securityContextImpl.getAuthentication().getName();
        // 登录名
//        System.out.println("Username:" + securityContextImpl.getAuthentication().getName());
        // 登录密码，未加密的
//        System.out.println("Credentials:" + securityContextImpl.getAuthentication().getCredentials());
//        WebAuthenticationDetails details = (WebAuthenticationDetails) securityContextImpl.getAuthentication().getDetails();
        // 获得访问地址
//        System.out.println("RemoteAddress:" + details.getRemoteAddress());
        // 获得sessionid
//        System.out.println("SessionId:" + details.getSessionId());
        // 获得当前用户所拥有的权限
//        List<GrantedAuthority> authorities = (List<GrantedAuthority>) securityContextImpl.getAuthentication().getAuthorities();
//        for (GrantedAuthority grantedAuthority : authorities) {
//            System.out.println("Authority:" + grantedAuthority.getAuthority());
//        }
        UserInfo userInfo = userService.details(username);
        mv.addObject("user", userInfo);
        mv.setViewName("user-details");
        return mv;
    }

    // 更新用户信息
    @RequestMapping("/update")
    public String update(UserInfo userInfo) {
        userService.update(userInfo);
        return "redirect:/pages/update-200.jsp";
    }

    // 查找用户，存在返回true
    @RequestMapping("findUserName")
    public @ResponseBody
    RegisterData findUserName(@RequestBody RegisterData data){
        Boolean flag = userService.findUsername(data);
        data.setFlag(flag);
        return data;
    }

}
