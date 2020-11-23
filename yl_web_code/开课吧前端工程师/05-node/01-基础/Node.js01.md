##Node.js01

##<img src="assets/logo.jpg" style="float:left;width:120px;margin-top:-48px;" />

- 课堂目标

  - 录播视频要点回顾
  - npm 包的注册与发布
  - yarn、cnpm、nvm 工具介绍

  - fs 加载模板 、 stream 方式加载模板
  - nodejs 中路由介绍
  - 新闻列表案例的 nodejs 实现

- 本节知识要点
  - Node.js 安装及使用
  - 通过 Node.js 搭建服务器
  - 模块化及自定义模块
  - 内置模块 fs 的使用
  - npm、cnpm、yarn、nvm 工具的使用
  - nodejs 加载页面

###node 录播视频回顾

---

- node 环境搭建

  - 下载安装（稳定版本，尝鲜版本）
  - 环境变量配置

- common.js 规范

  - 自定义模块
    - 导入：require；（“./”问题）导出：module.exports 或者 exports；
    - node_modules 里 package.json 配置；
    - node_modules 查找规则(向上查找)
  - 内置模块
    - 内置模块不需要安装，外置模块需要安装；

- npm 包管理器使用

  - npm i --save-dev（-D） --save（ -S ）； package.json
  - -g

  - npm root 、npm root -g

- fs 模块

  - 文件操作

    - 增、删、改、查 （同步及异步）

  - 目录操作
    - 删除非空目录

- buffer : toString();

- stream

### 其他工具介绍

- 注册与发布

  - 注册账号：[https://www.npmjs.com/](https://www.npmjs.com/) (邮箱验证)

  - npm adduser 输入刚刚注册好的用户名和密码 ；

    如果注册地址不对需要重新改回来：

    `npm config set registry https://registry.npmjs.org/ ` （官方地址）

    `https://registry.npm.taobao.org/` (淘宝源地址)

    查询源地址

    `npm config list`

  - 发布包

    - publish 命令

      发布成功后输出信息：

      <img src="/Users/yuweihai/Desktop/桌面/开课吧/细化过课/nodejs/assets/发布成功后.png" style="width:400px" />

      在 npm 网站上搜索到的包内容

      <img src="/Users/yuweihai/Desktop/桌面/开课吧/细化过课/nodejs/assets/搜索到的包.png" />

​

- cnpm 的安装及使用；

- yarn 包管理工具

  - ```js
    npm install -g yarn
    ```

  <img src="/Users/yuweihai/Desktop/桌面/开课吧/js001期相关/nodejs02/assets/yarn常用指令.png" />

  ​

- 使用 NVM（Node Version Manager）控制 Node.js 版本

  - nvm 是 mac 环境下管理 nodejs 的工具。在 windows 环境下推荐使用 nvmw 或者 nvm-windows；

    - Nvm-windows 下载地址 https://github.com/coreybutler/nvm-windows 下载 nvm-setup.zip

  - 安装 NVM

    - 在安装 nvm 之前需要一个 c++编译器，在 mac 上可以安装 Xcode 命令工具(已经安装可以忽略)

      `xcode-select --install`

    - 使用 curl 安装

      `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash`

    - 或者使用 wget 来安装

      `wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash`

  ​

  - NVM [github 的地址](https://github.com/creationix/nvm)可以查看最新版本

  ​

  - NVM 常用指令；

    ` nvm --version查看版本`

    `nvm install stable //安装最新稳定版nodejs`

    ` nvm install 8.11.1 //安装指定版本`

    ` nvm install 8.11 //安装 8.11.x系列最新版本`

    ` nvm ls-remote //列出远程服务器上所有可用的版本`

    ` nvm use 8.11.1 //切换到8.11.1版本`

    `nvm use 8.11 //切换到8.11.x最新版本`

    ` nvm use node //切换到最新版本`

    ` nvm alias default node //设置默认版本为最新版本`

    ` nvm ls //列出所有已经安装的版本`

###通过 fs 模块加载页面

- 普通方式加载页面
  - 路由区分
  - 加载页面
- 通过 stream 方式加载页面
  - 路由区分
  - 加载页面
  - 设置头部
  - 加载第三方资源

### node+cheerio 实现爬虫获取数据

- http://news.ifeng.com/ 新闻地址

- http.get()使用
- cheerio 来处理数据
- 文件方式储存数据

### 实现新闻列表页面

- 视图逻辑分离

- 读取页面
- 读取动态数据
- 设置头部引入其他资源
- 详细页显示

### 总结

- nodejs 的安装及使用
- 服务端及客户端

- 代码的前后端分离

- commonjs 模块化

- fs 模块的使用(文件操作及目录操作)

- 动态数据

- 实现新闻列表动态呈现

### 下期预告

- koa 框架

- koa-router

- koa-views

- Koa-static

- 新闻列表的 koa 实现
