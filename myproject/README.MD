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

### 其他说明
（1） User 模型被命名为内置应用叫 auth，它以命名空间 django.contrib.auth 的形式出现在 INSTALLED_APPS 配置中。

（2）如果我们没有为模型指定主键，Django会自动为我们生成它。 

（3）Python 附带了一个数据库 SQLIte 一个嵌入式的数据库引擎。 SQLite是一个产品级数据库。SQLite被许多公司用于成千上万的产品，
如所有Android和iOS设备，主流的Web浏览器，Windows 10，MacOS等。