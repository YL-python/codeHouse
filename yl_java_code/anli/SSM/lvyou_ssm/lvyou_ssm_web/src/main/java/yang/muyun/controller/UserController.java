package yang.muyun.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;
import yang.muyun.domain.Role;
import yang.muyun.domain.UserInfo;
import yang.muyun.service.IUserService;

import java.util.List;


@Controller
@RequestMapping("/user")
public class UserController {

    @Autowired
    IUserService userService;

    // 查询用户以及用户可以添加哪些角色
    @RequestMapping("/findUserByIdAndAllRole.do")
    public ModelAndView findUserByIdAndAllRole(@RequestParam(name = "id") Integer userId){
        ModelAndView mv = new ModelAndView();
        // 根据id查询用户
        UserInfo userInfo = userService.findById(userId);
        // 根据id查询可以添加的角色
        List<Role> otherRoles = userService.findOtherRole(userId);
        mv.addObject("user",userInfo);
        mv.addObject("roleList",otherRoles);
        mv.setViewName("user-role-add");
        return mv;
    }

    @RequestMapping("/findAll.do")
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public ModelAndView findAll(){
        ModelAndView mv = new ModelAndView();
        List<UserInfo> userList = userService.findAll();
        mv.addObject("userList",userList);
        mv.setViewName("user-list");
        return mv;
    }

    @RequestMapping("/save.do")
    @PreAuthorize("authentication.principal.username == 'tom'")
    public String save(UserInfo userInfo){
        userService.save(userInfo);
        return "redirect:findAll.do";
    }

    @RequestMapping("/findById.do")
    public ModelAndView findById(Integer id){
        ModelAndView mv = new ModelAndView();
        UserInfo userInfo = userService.findById(id);
        mv.addObject("user",userInfo);
        mv.setViewName("user-show");
        return mv;
    }

    @RequestMapping("/addRoleToUser.do")
    public String addRoleToUser(@RequestParam(name = "userId") Integer userId,@RequestParam(name = "ids") int[] roleIds){
        userService.addRoleToUser(userId,roleIds);
        return "redirect:findById.do?id="+String.valueOf(userId);
    }

}
