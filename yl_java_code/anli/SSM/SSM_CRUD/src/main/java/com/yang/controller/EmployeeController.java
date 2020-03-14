package com.yang.controller;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.yang.bean.Employee;
import com.yang.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

// 处理关于员工的CRUD 请求

@Controller
public class EmployeeController {

    @Autowired
    EmployeeService employeeService;

    // 查询所有员工
    @RequestMapping("/emps")
    public String getEmps(@RequestParam(value ="pn",defaultValue = "1") Integer pn,
                          Model model){
        // 起始页和每页条数
        PageHelper.startPage(pn,5);
        List<Employee> employeeList = employeeService.getAll();
        // 第二个参数是连续显示的页数
        PageInfo<Employee> pageInfo = new PageInfo<>(employeeList,5);
        model.addAttribute("pageInfo",pageInfo);
        return "list";
    }

}
