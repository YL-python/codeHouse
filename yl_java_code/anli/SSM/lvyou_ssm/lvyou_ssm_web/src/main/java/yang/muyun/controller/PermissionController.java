package yang.muyun.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import yang.muyun.dao.IPermissionDao;
import yang.muyun.domain.Permission;
import yang.muyun.domain.Role;
import yang.muyun.service.IRoleService;

import java.util.List;


@Controller
@RequestMapping("/permission")
public class PermissionController {

    @Autowired
    IPermissionDao permissionDao;

    @RequestMapping("/findAll.do")
    public ModelAndView findAll(){
        ModelAndView mv = new ModelAndView();
        List<Permission> permissionList = permissionDao.findAll();
        mv.addObject("permissionList",permissionList);
        mv.setViewName("permission-list");
        return mv;
    }

    @RequestMapping("/save.do")
    public String save(Permission permission){
        permissionDao.save(permission);
        return "redirect:findAll.do";
    }
}
