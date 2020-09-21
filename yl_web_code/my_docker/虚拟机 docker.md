虚拟机 docker

> 从零开始在虚拟机上安装使用docker

## 虚拟机的准备

###  CentOS下载

http://isoredirect.centos.org/centos/7/isos/x86_64#

![1600332232351](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600332232351.png)

```js
// CentOS 各个版本之间的区别如下：
1、CentOS-7-DVD版本：DVD是标准安装盘，一般下载这个就可以了。
2、CentOS-7-NetInstall版本：网络安装镜像。
3、CentOS-7-Everything版本：对完整版安装盘的软件进行补充，集成所有软件。
4、CentOS-7-LiveGnome版本：GNOME桌面版。
5、CentOS-7-KdeLive版本：KDE桌面版。
6、CentOS-7.0-livecd版本：光盘上运行的系统，类拟于winpe
```

### VMware建立虚拟机

+ 新建
+ 自定义

![1600332854567](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600332854567.png)

+ 默认下一步

![1600332883928](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600332883928.png)

+ 稍后安装操作系统

![1600332906999](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600332906999.png)

+　自己是啥就选啥

![1600332993287](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600332993287.png)

+ 命名和路径自定义，随意

![1600333077799](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333077799.png)

+ 默认

![1600333099268](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333099268.png)

+ 一般1G或者2G 足够用了 

![1600333151861](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333151861.png)

+ 网络选择 NAT

![1600333174504](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333174504.png)

+ 后面二个用推荐的就行

![1600333212290](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333212290.png)

![1600333224153](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333224153.png)

+ 穿件虚拟磁盘，分配的空间20G，不是真的有20G，是虚拟的 不要慌

![1600333322880](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333322880.png)

![1600333328303](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333328303.png)

![1600333342473](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333342473.png)

+ 然后可以自定义硬件，一般用不上声卡和打印机啥的，随意关闭 然后确定就有了。

![1600333502434](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333502434.png)

![1600333640857](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333640857.png)

右侧面板找到自己刚刚创建的虚拟机，右击设置，CD/DVD 使用iso文件找到刚刚下载的系统就行，然后开启此虚拟机。

+ 选择第一个  安装，第二个选项是检查系统在安装，一般下下来的系统没有问题的，就算有问题那咱也到不了这一步。

![1600333787684](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333787684.png)

+ 选择语言，虽然极力推荐英文，但是因为我是老手了，而且想试试中文的就来看看中文是啥样的（绝对不要因为我看不懂英文）

![1600333959137](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600333959137.png)

+ 安装这里注意一下这个软件选择，一般是两种，一个是常见的黑框框，极力推荐小白选这个，还有一个就是和windows10一样的图形界面。

![1600334182128](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600334182128.png)

![1600334380845](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600334380845.png)

我选的是最小安装

+ 设置root 用户密码   这个随意  写一下我的怕以后忘记了  hzz123,./

![1600334493962](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600334493962.png)

+ 下面有进度条提示，等待安装完成咯

![1600334533839](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600334533839.png)

+ 可以创建其他用户，但是吧 咱新手，用root用户啥权限都有，之后可以横着走路，当然可以的话也要学学分组，多用户这些方面的。

![1600335118047](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600335118047.png)

重启登录用户，说明一下 Linux系统输入密码的时候是看不见的，所以输入的时候啥都没有是正常的。

### 配置网络

> 辛苦辛苦，虚拟机咱是弄完了，现在来深入

+ 第一步当然是联网

![1600335216767](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600335216767.png)

`ping` 一下百度发现出错，说明咱还没联网。

+ 遇到问题不要慌一步步解决

![1600336328188](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600336328188.png)

 s32是系统生成的每个人不一样

![1600336408340](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600336408340.png)

吧最后的  ONBOOT改成yes 然后  `service network restart`  重启网络服务就可以ping通百度了

### 静态Ip 设置 

+ 嘤嘤嘤 `centos6`是用`ifconfig`查看ip，7用`ip addr`  搞得我百度半天我`ifconfig`指令为啥没用

+ 查看网关，后面要用

![1592480111994](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1592480111994.png)

![1600336328188](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600336328188.png)

+ 依然是修改这个文件

![1600336905804](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600336905804.png)


```Python
# 修改下面两个
BOOTPROTO=static		# 改成静态
ONBOOT=yes				# 网卡自启动，之前改过了
# 添加下面三个
GATEWAY=192.168.13.2   # 网关
IPADDR=192.168.13.100  # 自定义静态IP 前3个不动和网关一样，后面一个是自定义的
NETMASK=255.255.255.0  # 掩码 默认就是这个
```

+ `systemctl restart network` 指令重启网络   `ip addr` 查看网络

![1600337333309](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600337333309.png)

完美，不放心的可以重启一下再来看看。

### xshell 链接虚拟机

![1600339458225](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600339458225.png)

常规操作不多说。

![1600339478995](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600339478995.png)

### 关闭防火墙

```js
firewall-cmd --state  // 查看防火墙状态
systemctl stop firewalld.service  // 关闭防火墙  
systemctl disable firewalld.service  // 禁止开机自启动
```

## 安装 docker

> http://get.daocloud.io/
>
> https://developer.aliyun.com/article/110806
>
> https://yeasy.gitbook.io/docker_practice/

### 0.卸载旧版本

```c++
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

### 1.下载Dcoker依的赖环境

```c++
# 想安装Docker，需要先将依赖的环境全部下载下来，就像Maven依赖JDK一样
yum -y install yum-utils device-mapper-persistent-data lvm2
```

### 2.指定Docker镜像源

```c++
# 默认下载Docker会去国外服务器下载，速度较慢，可以设置为阿里云镜像源，速度更快
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

### 3.安装Docker

```c++
yum install docker-ce docker-ce-cli containerd.io
```

### 4.启动Docker并测试

```c++
# 安装成功后，需要手动启动，设置为开机启动，并测试一下 Docker
# 启动docker服务
systemctl start docker
# 查看docker服务
systemctl status docker
# 设置开机自动启动
systemctl enable docker
# 测试
docker run hello-world
```

### 5.添加中国下载源

```c++
# 新建或更新文本文件
vi /etc/docker/daemon.json
# 添加下面内容
{
    "registry-mirrors":["http://hub-mirror.c.163.com"]
}
# 官方镜像：https://registry.docker-cn.com   官方镜像还是很慢
# 网易镜像：http://hub-mirror.c.163.com
# 阿里镜像：需要有阿里云服务器，然后自己百度吧
# 重启
systemctl daemon-reload
systemctl restart docker
```

```c++
docker run --name docker-mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:5.7.4
```

## docker 基本操作

> 指令说明大全：https://www.runoob.com/docker/docker-command-manual.html
>
> 或者使用--help参数查看说明
>
> 例如 docker --help	docker images --help	docker run --help

### 0.基本概念介绍

Docker 包括三个基本概念:

- **镜像（Image）**：Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 ubuntu:16.04 就包含了完整的一套 Ubuntu16.04 最小系统的 root 文件系统。
- **容器（Container）**：镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的类和实例一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。
- **仓库（Repository）**：仓库可看成一个代码控制中心，用来保存镜像。

Docker 使用客户端-服务器 (C/S) 架构模式，使用远程API来管理和创建Docker容器。

Docker 容器通过 Docker 镜像来创建。

容器与镜像的关系类似于面向对象编程中的对象与类。

### 1.镜像的基本操作

+ 1.1 查看本地镜像列表

```c
# 指令
docker images
# 说明
REPOSITORY：表示镜像的仓库源
TAG：镜像的标签
IMAGE ID：镜像ID
CREATED：镜像创建时间
SIZE：镜像大小
```

+ 1.2 搜索镜像

```c
# 指令
docker search httpd
# 说明
NAME: 镜像仓库源的名称
DESCRIPTION: 镜像的描述
OFFICIAL: 是否 docker 官方发布
stars: 类似 Github 里面的 star，表示点赞、喜欢的意思。
AUTOMATED: 自动构建。
```

+ 1.3 下载镜像

```c
# 指令
docker pull 镜像名称[:tag]
# 举个栗子:docker pull daocloud.io/library/tomcat:8.5.15-jre8
# 举个栗子:docker pull mysql:5.7.4
```

+ 1.4 删除镜像

```c
# 镜像会占用磁盘空间，可以直接手动删除，标识通过查看获取
docker rmi 镜像的标识
```

### 2.容器的基本操作

> 镜像相当于是一个安装包，容器相当于给这个安装包提供了一个运行的环境

+ 2.1运行容器

```c
#运行容器需要定制具体镜像，如果镜像不存在，会直接下载
docker run 镜像的标识|镜像的名称[:tag]]
# 常用的参数
-t: 在新容器内指定一个伪终端或终端。
-i: 允许你对容器内的标准输入 (STDIN) 进行交互。
-d: 后台运行容器，并返回容器ID；
-P: 随机端口映射，容器内部端口随机映射到主机的端口
-p: 指定端口映射，格式为：主机(宿主)端口:容器端口
--name="XXX": 为容器指定一个名称；
-e XXX="YYY": 设置环境变量；
# 举个栗子
docker run --name docker-mysql -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3306 mysql:5.7.4
# 运行的镜像是 mysql:5.7.4，用--name取个名字叫  docker-mysql，-d 在后台运行，-p 吧主机的3306端口和容器内的3306端口连接，-e给容器内设置了一些MYSQL_ROOT_PASSWORD这个参数的值是 root
```

+ 2.2查看容器

```c
# 指令
docker ps  # 默认是查看正在运行的容器 -a参数可以查看所用的容器
# 说明
CONTAINER ID: 容器 ID。
IMAGE: 使用的镜像。
COMMAND: 启动容器时运行的命令。
CREATED: 容器的创建时间。
PORTS: 容器的端口信息和使用的连接类型（tcp\udp）。
NAMES: 自动分配的容器名称。
STATUS: 容器状态。
	状态有7种：created（已创建），restarting（重启中），running（运行中），removing（迁移中），paused（暂停），exited（停止），dead（死亡）
```

+ 2.3停止 / 重启容器

```c
# 指令 
docker stop <容器 ID>/容器名称
docker restart <容器 ID>/容器名称
```

+ 2.4删除容器

```c
# 指令 
docker rm <容器 ID>/容器名称  # rm删除容器  rmi删除镜像
# 常用参数
-f : 通过SIGKILL信号强制删除一个运行中的容器
-l : 移除容器间的网络连接，而非容器本身
-v : 删除与容器关联的卷
```

+ 和容器内的交互

```c++
# 需求是咱现在有容器了，需要和容器交互 在run 的时候可以用 -it进行交互，但是-d是后台运行的应该怎么交互呢
# 指令
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
-d :分离模式: 在后台运行
-i :即使没有附加也保持STDIN 打开
-t :分配一个伪终端
# 举个栗子 登录mysql并且创建一个数据库
docker exec -it docker-mysql bash
```

![1600409608310](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600409608310.png)

## docker 应用

### mysql

```c++
# docker 部署mysql
docker run --name docker-mysql -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3306 mysql:5.7.4
```

![1600349052022](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600349052022.png)

### node.js

```c
# 下载并运行 node
docker run -itd --name docker-node node
# 查看运行镜像
docker ps
# 进入node
docker exec -it docker-node bash
# 查看node版本
ndoe -v
```

![1600410708159](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600410708159.png)

### redis

```c
# 下载并运行 redis  设置密码是 mypassword
docker run -d --name docker-redis -p 6379:6379 redis --requirepass "mypassword"
# 查看运行镜像
docker ps
# 进入 redis
docker exec -it docker-redis /bin/bash
# 启动 redis 客户端
redis-cli
#添加数据
set test 1
```

![1600411563900](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600411563900.png)

客户端工具连接成功并且有刚刚插入的数据

![1600411701893](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600411701893.png)

### mongodb

```c
# 下载并运行 mongo  设置 需要密码登录
docker run -itd --name docker-mongo -p 27017:27017 mongo --auth
# 查看运行镜像
docker ps
# 进入 mongo
docker exec -it docker-mongo mongo admin
# 新建用户
db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'}]});
# 用新用户登录
db.auth('admin', '123456')
```

![1600413057468](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600413057468.png)

robo3t 测试连接成功

![1600413219058](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600413219058.png)

### nginx

```c
# 下载并运行 nginx  设置 需要密码登录
docker run -itd --name docker-nginx -p 27017:27017 mongo --auth
# 查看运行镜像
docker ps
```

![1600413635261](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600413635261.png)

访问成功

![1600413678514](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600413678514.png)

### tomcat

```c
# 主机文件夹  /root/docker-tomcat/demo/index.html
# 文件的内容是 <h1>这里是docker环境下的Tomcat</h1>
# 下载
docker pull tomcat:8
# 运行
docker run --privileged=true -v /root/docker-demo:/usr/local/tomcat/tomcat8/webapps -p 8082:8080 --name docker-tomcat tomcat:8
# 参数说明
--privileged=true  # 允许docker挂载文件
# -v 表示文件关联 前面是主机路径，后面是容器内的路径
-v /root/docker-demo:/usr/local/tomcat/tomcat8/webapps
```

![1600416828752](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600416828752.png)

这个图可以看出来我们的Tomcat是跑起来了，但是找主文件的时候没有找到就报了404错误

我进入容器内发现原因是 Tomcat8的webapps目录是空的当然就会报404，还有一个webapps.dist文件夹内装的是我们之前熟悉的 webapps文件

![1600417009489](%E8%99%9A%E6%8B%9F%E6%9C%BA%20docker.assets/1600417009489.png)

说明我们的文件关联也是没问题的，乱码是我就写了h1标签内有些文件编码方式就乱码啦

### ----高级一点

> 既然说高级一点说明之前的都不是很高级
>
> 对于入门来说当然就已经可以了，学到了用docker部署环境，在Tomcat还学到了文件挂载
>
> 问题：装了nginx怎么在容器内做负载均衡反向代理，Tomcat部署项目还有没有别的方法，运行node项目应该怎么办？
>
> 高级就是来解决这些的

### docker nginx 负载均衡

### docker 部署nodejs项目

```c
https://nodejs.org/zh-cn/docs/guides/nodejs-docker-webapp/
```



## docker-compose

> http://get.daocloud.io/ 

### 1.下载

```c++
# 下载
sudo curl -L https://get.daocloud.io/docker/compose/releases/download/1.27.3/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    
# 赋予权限
sudo chmod +x /usr/local/bin/docker-compose

# 创建软链
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# 测试是否安装成功
docker-compose --version
    
# 卸载 docker-compose 是二进制的文件，只要全部删掉就行
rm -rf /usr/bin/docker-compose
```

### 2.入门使用

```c
# 在需要的位置新建 docker-compose.yml 文件
version: '3'
services:
  mysql1:
    image: mysql
    environment:
    - MYSQL_ROOT_PASSWORD=123456
    ports:
    - 28002:3306

  mysql2:
    image: mysql
    environment:
    - MYSQL_ROOT_PASSWORD=123456
    ports:
    - 28003:3306
```

### 3.指令介绍

```c
https://yeasy.gitbook.io/docker_practice/compose/commands
```

### 4.docker-compose.yml文件说明

```c
https://yeasy.gitbook.io/docker_practice/compose/compose_file
```

