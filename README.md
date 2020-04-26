# WikiList
使用 Django 创建一个wiki列表，帮忙组员管理和查阅内部分享的wiki。

开发的大致流程

- 配置管理后台、数据库
  - Sqlite
  - django管理后台
- 配置前端页面、编写界面
  
  - 简单的html
- 前端与后台交互
  - URL重定向
  - 搜索功能
- 打包部署发布
  - nginx+uwsgi+django
  
  - 局域网部署
  
    ```swift
    在settings.py里找到改成ALLOWED_HOSTS  = ['*']
    在命令行启动服务时改成局域网ip，比如我的就是 
    python manage.py runserver 192.168.0.101:9000
    其他电脑上输入
    管理后台：http://192.168.0.101:9000/admin/wikiPage/wiki/
    前端页面：http://192.168.0.101:9000/wikiPage/
    
    具体流程
    1. 打开终端，并获取 IP(取第一个)
    ifconfig | grep inet | grep -v inet6 | grep -v 127 | cut -d ' ' -f2
    2. 开启服务
    python manage.py runserver IP:端口  
    3. 局域网内用户就可以使用了
    IP:端口/路径 
    ```
  
    





  



