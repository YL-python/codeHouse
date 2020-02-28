# markdown语法
## 二级标题
### 三级标题
#### 四级标题


***
分割符有三种写法
***
---
___
分割符有三种写法：三个*，三个-，三个_


***
一个*包围是斜体*  
两个**包围是粗体**  


***
>引用是啥
>>引用是这样啊
>>>引用原来还可以多个


***
标题1
===
标题2
---


***
- 无序列表
- 无序列表
- 空格不能少
* 还可以用 * - +
+ 有点意思


***
1. 有序列表
8. 有序列表8
2. 有序列表2
3. 不知道有啥区别


***
- 列表嵌套
 - 这样吗
 - 不清楚啊
     + emm
     + 加了好多空格才实现三级嵌套
 * + - * 三个符号可以混用
 * 不过不推荐 太花里胡哨不好


***
[这里是超链接](https://blog.csdn.net/qcx321/article/details/53780672#1-%E5%BC%BA%E8%B0%83 "快点我")


***
![图片连接](http://img.netbian.com/file/2019/0920/a7b61fd224f1b0e7b9781229ac3f3d0c.jpg "图片地址不存在好像就不会显示")
加了一个感叹号


***
添加自动连接  
<https://blog.csdn.net/qcx321/article/details/53780672#1-%E5%BC%BA%E8%B0%83>


***
[索引连接][索引内容]
索引连接可以写在任意地方，索引内容  随意

[索引内容]:https://blog.csdn.net/qcx321/article/details/53780672#1-%E5%BC%BA%E8%B0%83


***
代码块  
``` python
@requires_authorization
def somefunc(param1='', param2=0):
    '''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1) or None
class SomeClass:
    pass
>>> message = '''interpreter
... prompt'''
```

用tab 或者四个空格也行  

	val s = "hello Markdown"
	println( s )
	val s = "hello Markdown"
    println( s )


***
设置字体  
<font face="黑体">我是黑体字</font>  
<font face="微软雅黑">我是微软雅黑</font>  
<font face="STCAIYUN">我是华文彩云</font>  
<font color=#0099ff size=12 face="黑体">黑体</font>  
<font color=#00ffff size=3>null</font>  
<font color=gray size=5>gray</font>  


***
转义字符  
\\ 反斜杠  
\` 反引号  
\* 星号  
\_ 下划线  
\{\} 大括号  
\[\] 中括号  
\(\) 小括号  
\# 井号  
\+ 加号  
\- 减号  
\. 英文句号  
\! 感叹号  


***
表格  
| Tables        | Are           | Cool  |  
| ------------- |:-------------:| -----:|  
| col 3 is      | right-aligned | $1600 |  
| col 2 is      | centered      |   $12 |  
| zebra stripes | are neat      |    $1 |