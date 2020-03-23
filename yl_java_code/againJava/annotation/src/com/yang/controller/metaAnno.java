package com.yang.controller;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**

 元注解：用于描述注解的注解
 @Target：描述注解能够作用的位置
    ElementType.TYPE  定义注解只能作用在 类上
    ElementType.METHOD  定义注解只能作用在 方法上
    ElementType.FIELD  定义注解只能作用在 成员方法上

 @Retention：描述注解被保留的阶段
 @Documented：描述注解是否被抽取到api文档中
 @Inherited：描述注解是否被子类继承
    子类会默认继承父类的注解

 *
 */
@Target(value = {ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
public @interface metaAnno {
}
