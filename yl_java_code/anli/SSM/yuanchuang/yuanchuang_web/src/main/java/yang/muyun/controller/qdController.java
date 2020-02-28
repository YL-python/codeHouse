package yang.muyun.controller;

import com.github.pagehelper.PageInfo;
import org.omg.CORBA.MARSHAL;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextImpl;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;
import yang.muyun.domain.UserInfo;
import yang.muyun.domain.UserSignIn;
import yang.muyun.service.IUserService;
import yang.muyun.service.IUserSignInService;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

@Controller
@RequestMapping("/qd")
public class qdController {

    @Autowired
    IUserSignInService userSignInService;

    // 发表签到
    @RequestMapping("/signin")
    public String signin(UserSignIn userSignIn, HttpServletRequest request) {
        SecurityContextImpl securityContextImpl = (SecurityContextImpl) request.getSession().getAttribute("SPRING_SECURITY_CONTEXT");
        String username = securityContextImpl.getAuthentication().getName();
        userSignIn.setQdUsername(username);
        userSignInService.signin(userSignIn);
        return "redirect:/pages/main.jsp";
    }

    // 查询所有签到
    @RequestMapping("/AllInformation")
    public ModelAndView AllInformation(HttpServletRequest request,@RequestParam(name = "page", defaultValue = "1") Integer page) {
        ModelAndView mv = new ModelAndView();
        SecurityContextImpl securityContextImpl = (SecurityContextImpl) request.getSession().getAttribute("SPRING_SECURITY_CONTEXT");
        String username = securityContextImpl.getAuthentication().getName();
        // pageInfo 是一个分页bean
        List<UserSignIn> userSignInList = userSignInService.findAll(username, page);
        PageInfo pageInfo = new PageInfo(userSignInList);
        mv.addObject("pageInfo",pageInfo);
        mv.setViewName("qd-details");
        return mv;
    }
}
