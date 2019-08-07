### 项目链接
https://github.com/pythonzhichan/django-beginners-guide

### Django 常用的命令
####  启动一个新项目 
django-admin startproject myproject

####  启动服务
python manage.py runserver

####  创建一个新的应用程序
django-admin startapp boards

####  迁移模型 
python manage.py makemigrations

#### 检验迁移生成的 sql 语句
python manage.py sqlmigrate boards 0001

#### 将生成的迁移文件应用到数据库 
python manage.py migrate

#### 执行 django 的测试套件 
python manage.py test

#### 创建一个管理员账户
python manage.py createsuperuser 

#### 在测试时显示更加详细的信息， 可将verbosity的级别设置得更高一点
Verbosity决定了将要打印到控制台的通知和调试信息量; 0是无输出，1是正常输出，2是详细输出。
python manage.py test --verbosity=2

#### 使用 manage.py 工具加载项目启动 python shell
python manage.py shell
与直接输入 python 指定来调用交互控制台相似，除此之外，项目将被添加到 sys.path 并加载 Django。
这意味着我们可以在项目导入我们的模型和其他资源并使用它。 

### 关于 Django 的模型管理器 
每个Django模型都带有一个特殊的属性; 我们称之为模型管理器(Model Manager)。
你可以通过属性objects 来访问这个管理器，它主要用于数据库操作。
#### 使用模型管理器创建新的对象 
board = Board.objects.create(name='Python', description='General discussion about Python.')

#### 使用模型管理器查看数据中现有的数据 
Board.objects.all()

#### 使用模型管理器来查询数据库并且返回单个对象 但是这样如果查询不存在的对象就会引发异常
django_board = Board.objects.get(id=1)

#### get方法的参数可以是模型的任何字段，但最好使用可唯一标识对象的字段来查询。否则，查询可能会返回多个对象，这也会导致异常。
Board.objects.get(name='Django')

#### 查询区分大小写 
Board.objects.get(name='django')

### 用来绘制模型图的工具 
http://staruml.io/
### 绘制网页线框的工具 
https://www.draw.io/
### 寻找一些比较好用的背景图 
https://www.toptal.com/designers/subtlepatterns/ 

### 其他说明
（1） User 模型被命名为内置应用叫 auth，它以命名空间 django.contrib.auth 的形式出现在 INSTALLED_APPS 配置中。

（2）如果我们没有为模型指定主键，Django会自动为我们生成它。 

（3）Python 附带了一个数据库 SQLIte 一个嵌入式的数据库引擎。 SQLite是一个产品级数据库。SQLite被许多公司用于成千上万的产品，
如所有Android和iOS设备，主流的Web浏览器，Windows 10，MacOS等。

(4) 在与 manage.py 同级的位置创建 templates 文件夹

(5) 在 Python shell 中调试项目配置： 

```
from django.conf import settings

settings.BASE_DIR
'/Users/vitorfs/Development/myproject'

import os

os.path.join(settings.BASE_DIR, 'templates')
'/Users/vitorfs/Development/myproject/templates'
```

(6)在每个 app 的 tests 文件中编写单元测试

(7) 什么是静态文件： 静态文件是指 CSS，JavaScript，字体，图片或者是用来组成用户界面的任何其他资源。

实际上，Django 本身是不负责处理这些文件的，但是为了让我们的开发过程更轻松，
Django 提供了一些功能来帮助我们管理静态文件。
这些功能可在 INSTALLED_APPS 的 django.contrib.staticfiles 应用程序中找到
（译者：Django为了使得开发方便，也可以处理静态文件，而在生产环境下，静态文件一般直接由 Nginx 等反向代理服务器处理，
而应用工服务器专心负责处理它擅长的业务逻辑）。

(8) 关于前端框架： 
市面上很多优秀前端组件框架，我们没有理由继续用简陋的HTML文档来渲染】。
我们可以轻松地将Bootstrap 4添加到我们的项目中。Bootstrap是一个用HTML，CSS和JavaScript开发的前端开源工具包。

(9) 在使用管理后台之前我们一直使用 shell 来添加内容。 

(10) 使用 Django Admin的一个很好的例子就是用在博客中; 它可以被作者用来编写和发布文章。
另一个例子是电子商务网站，工作人员可以创建，编辑，删除产品。

(11) URL 调度器（dispatcher） 和 URLconf (URL configuration) 是 Django 应用中的基础部分。
在开始的时候，这个看起来让人很困惑；我记得我第一次开始使用 Django 开发的时候也有一段时间学起来很困难。
事实上，Django开发团队正在致力于将路由语法简化（译注：就是将原来url函数替换成 path 函数，
目前django2.0已经正式使用新的路由语法）

一个项目可以有很多 urls.py 分布在多个应用（app）中。Django 需要一个 url.py 作为入口。
这个特殊的 urls.py 叫做 根路由配置（root URLconf）。它被定义在 settings.py 中。
它已经自动配置好了，你不需要去改变它任何东西。

当 Django 接受一个请求(request)， 它就会在项目的 URLconf 中寻找匹配项。
他从 urlpatterns 变量的第一条开始，然后在每个 url 中去匹配请求的 URL。

如果 Django 找到了一个匹配路径，他会把请求(request)发送给 url 的第二个参数 视图函数（view function）。
urlpatterns 中的顺序很重要，因为 Django 一旦找到匹配就会停止往后搜索。
如果 Django 在 URLconf 中没有找到匹配项，他会通过 Page Not Found 的错误处理代码抛出一个 404 异常。

 这是 url 函数的剖析：
```
def url(regex, view, kwargs=None, name=None):
    # ...
```

regex： 匹配 URL patterns 的正则表达式。注意：正则表达式会忽略掉 GET 或者 POST 后面的参数。
在一个 http://127.0.0.1:8000/boards/?page=2 的请求中，只有 /boards/ 会被处理。

view： 视图函数被用来处理用户请求，同时它还可以是 django.conf.urls.include 函数的返回值，
它将引用一个外部的urls.py文件，例如，你可以使用它来定义一组特定于应用的 URLs，使用前缀将其包含在根 URLconf 中。

kwargs：传递给目标视图函数的任意关键字参数，它通常用于在可重用视图上进行一些简单的定制，我们不是经常使用它。
name:： 该 URL 的唯一标识符。这是一个非常重要的特征。要始终记得为你的 URLs 命名。
所以，很重要的一点是：不要在 views(视图) 或者 templates(模板) 中硬编码 URL，而是通过它的名字去引用 URL。

（12） PK or ID？ PK 表示主键（Primary key），这是访问模型的主键ID的简写方法，所有Django模型都有这个属性，
更多的时候，使用pk属性和使用id是一样的，这是因为如果我们没有给model定义主键时，
Django将自动创建一个 AutoField 类型的字段，名字叫做 id，它就是主键。
如果你给model定义了一个不同的主键，例如，假设 email 是你的主键，
你就可以这样访问：obj.email 或者 obj.pk，二者是等价的。

(13) 关于表单： Forms(表单) 用来处理我们的输入。这在任何 web 应用或者网站中都是很常见的任务。
标准的做法是通过 HTML 表单实现，用户输入一些数据，将其提交给服务器，然后服务器处理它。

(14) Django 使用 CSRF Token(Cross-Site Request Forgery Token) 保护所有的 POST 请求。
这是一个避免外部站点或者应用程序向我们的应用程序提交数据的安全措施。应用程序每次接收一个 POST 时，
都会先检查 CSRF Token。如果这个 request 没有 token，或者这个 token是无效的，它就会抛弃提交的数据。

(15) 接下来要创建 django 的用户身份识别系统，实现注册、登录、注销、密码重置和密码修改的整套流程。
所有身份认证相关的内容都将在另一个应用中，这样能更良好的组织代码。 
django-admin startapp accounts


