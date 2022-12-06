# 一个懒人的物联网后端学习记录

![开启懒人模式](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//006r3PQBjw1f9zux1ikmcj30b40b4q3t.jpg)

## 项目简介

这个项目主要实现了两个主要功能

- 接收并存储传感器上传的数据,
- 按条件展示传感器数据,
- 通过mqtt给硬件发送控制指令,

共计约1000行代码.

作为一个懒人,我记不住也不想到处搜索运维相关的linux命令,也不想频繁的修改配置文件,于是通过python写了些自动化的脚本,这样用起来感觉就舒服的多了.

![爽](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//9150e4e5gw1f9kyzrw3f8j207f06o0sq.jpg)

### 适合的人群

- 对python感兴趣,想要开发轻量级的后端应用
- 对性能要求不高,图个方便

## 来自懒人的推荐

我觉得我这个项目还是蛮适合懒人用的,下边是我推荐它的理由:

- 懒人运维

  曾经天真的以为在windows上边写好一个应用,不就是丢到服务器上运行嘛,能有啥难的. 结果发现还真不是那么容易, 之前还在服务器上装maven,装tomcat啥的,好麻烦啊. 

  现在只要服务器上有个能用的python(版本>3.9最好),然后有个git(用来克隆代码,或者有啥别的方法能把文件夹丢到服务器上也行),最后服务器是Centos或者ubuntu系统,就能愉快的运行后端了.

- 开机自启

  因为作者开发的过程中偶尔碰到奇奇怪怪的bug的时候很懵逼,但是重新启动一下app能解决很多问题,于是乎给它配置好了开机自启,这样出bug了我就重启服务器,一句`sudo reboot`解决90%的问题

- 可以一句话就挂在后台任意端口运行

  ```python
  python3 run_app.py 
  python3 run_app.py 443
  ```

- 一句话关闭app或杀掉占用端口的进程

  ```python
  python3 kill_port.py 80
  ```

- 通过配置文件配置数据库连接,mqtt_id等,部署到不同的环境只需要对配置文件稍作修改即可

  作为一个懒人,我连配置文件都懒得改,因为我的虚拟机,本机,服务器都不是同一个系统,可以很容易区分出来.我是这样写的:

  ![image-20221206192956902](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221206192956902.png)

  只要在`config_files`下修改`appConfig.yml`和`load_total_project_configs.py`中稍作修改即可到处运行.

- 容易安装

  1. 克隆代码

  ```sh
  https://github.com/LiRunJi/My_IOT_Learning.git 
  ```

  ```sh
  cd My_IOT_Learning
  ```

  2. 安装对应的python包

  ```python
  pip3 install requitements.txt
  ```

  3. [安装emqx](https://www.emqx.io/zh/downloads?os=Ubuntu) (三行代码)

  4. 修改配置文件,把数据库的url和密码换成自己的

  5. 启动app

     ```sh
     python3 run_app.py
     ```

  然后就可以愉快的运行了.

- 美观又方便测试的接口文档

  这也是我选择用FastAPI的理由,它自带可以测试接口用的网页,并且网页很漂亮,很容易给网页添加注释.

  ![image-20221206202711142](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221206202711142.png)
  
- 容易看懂的代码

- 传感器数据采集

- 传感器数据查询的接口

- 前端可以调用这里的http接口通过mqtt发送数据

## 项目结构

![image-20221206191128543](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221206191128543.png)

## 来自懒人的收获

- 折腾了一个云服务器,有公网ip就是爽啊,不仅可以挂自己写的东西,还可以做远程VNC桌面控制,顺便了解了些linux相关的应用(虽然一开始用不习惯非常痛苦)
- 有了一套传输数据与存储数据的方法,折腾硬件或者是人工智能相关的可以通过一种简单的方式接入到后端, 享受后端带来的数据存储,与其它端沟通的服务, 给自己定制一套智能家居倒是舒服极了
- 对python更熟悉了

![爽翻了（鸭鸭）_爽翻表情](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//415f82b9ly1fpg6be2pudj20c8096759.jpg)

## 使用方式

目前可以作为一个模板和一个工具来用,包括了一些方便运维的脚本.

### 1. 安装所需的环境

推荐在Ubuntu虚拟机上装一个Pycharm,这样的环境非常舒服.

1. 克隆代码

```sh
https://github.com/LiRunJi/My_IOT_Learning.git 
```

```sh
cd My_IOT_Learning
```

2. 安装对应的python包

```python
pip3 install requitements.txt
```

3. [安装emqx](https://www.emqx.io/zh/downloads?os=Ubuntu) (三行代码)

4. 修改配置文件,把数据库的url和密码换成自己的

5. 启动app

   ```sh
   python3 run_app.py
   ```

然后就可以愉快的运行了.

运行之后会生成这么一个接口文档:

![image-20221206203702624](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221206203702624.png)

### 2. 修改为自己的配置

![image-20221206205900900](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221206205900900.png)

### 3. 在模板里增加自己的业务

![image-20221206191128543](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221206191128543.png)

### 4. 在主函数中挂载自己的业务

```python
from DianDongChe.Services import \
    HardhareControlService,\
    DataAddService,\
    DataQueryService,\
    PeopleService,\
    BaoJingService
app.include_router(HardhareControlService.router)
app.include_router(DataAddService.router)
app.include_router(DataQueryService.router)
app.include_router(PeopleService.router)
app.include_router(BaoJingService.router)
```



## 鸣谢

多亏了网上大把的优质教程和开源项目,可以让一个只会一些python基础应用的人基于python做出令自己非常开心的App.

- [FastAPI四小时快速入门](https://www.youtube.com/watch?v=7t2alSnE2-I&t=5137s)
- [SQL四小时快速入门](https://www.youtube.com/watch?v=HXV3zeQKqGY)
- [学生免费用的Pycharm](https://www.jetbrains.com/zh-cn/pycharm/)
- [FastAPI (tiangolo.com)](https://fastapi.tiangolo.com/zh/)
- [SQLAlchemy - The Database Toolkit for Python](https://www.sqlalchemy.org/)
- [PyYAML · PyPI](https://pypi.org/project/PyYAML/)
- [Python的PyYAML模块详解_bossenc的博客-CSDN博客_pyyaml](https://blog.csdn.net/swinfans/article/details/88770119)
- [paho-mqtt · PyPI](https://pypi.org/project/paho-mqtt/)
- [EMQX ](https://www.emqx.io/docs/zh/v5.0/getting-started.html)
- [在服务器上装python3.10](https://zhuanlan.zhihu.com/p/491817098)
- [表情包来源](https://www.fabiaoqing.com/)
- 还有一些教程,当时觉得很有用,但是现在记不得了

![给大佬递心](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//006qir4oly1g2xsq3njonj30500500su.jpg)

## 项目的缺陷

由于写这个项目的适合还是新手入门,难免有很多缺陷,后续如果有时间的话或许会缝缝补补修补这些缺陷.



- 数据层SQL写的并不利索,和数据库直接会多传递一些没用的数据

  这是因为当时懒得写成sql语句了... 

- 传递数据并没有用加密,全是无加密的http

- 起名字起的有时候很迷惑

- mqtt客户端不定期的会掉线然后重启,目前的解决办法是多发几遍,直到发出去了为止

- 一些奇奇怪怪的接口

- 代码水平不高

  入门的过程写的,大家见谅哈 

  ![嘿嘿](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//ceeb653ely8gs9t2po1glj2046046js0.jpg)

  

