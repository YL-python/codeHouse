package com.yang.service;

import com.yang.bean.Employee;
import org.springframework.stereotype.Service;

import java.util.List;


public interface EmployeeService {
    List<Employee> getAll();

}
