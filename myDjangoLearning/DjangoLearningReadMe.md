## 1.执行```django-admin.py startproject yourProjectName```
创建一个新的Django项目,项目名就是你填写的"yourProjectName"

## 2.新创建的Django项目结构如下:
### 2.1 最外层是yourProjectName文件夹

### 2.2 里面是manage.py和一个yourProjectName文件夹
这个manage.py的作用:
把该工程的包加入了 sys.path ;以后可以直接在代码中引用该工程中其他的包
加载 DJANGO_SETTINGS_MODULE,指明该工程的配置文件是 yourProjectName/settings.py
最主要的是它包裹了 django-admin.py 的一些函数，让你可以通过它来操作整个工程

### 2.3 这个yourProjectName文件夹里面包含了一些初始文件:
#### 2.3.1 __init__.py:
这个文件是Python 语言的一种习惯,经常为空文件.
主要是告诉工程这是一个包(Package),防止不经意间因为包名为诸如String之类的字符串而引起的混乱

#### 2.3.2 settings.py:
此前我们提到了manage.py的第二件工作便是指定了它是工程的配置文件，那它配置了些什么呢？
主要设置了关于数据库，后台管理等配置

#### 2.3.3 url.py:
它负责把客户的请求翻译成函数调用,关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数

#### 2.3.4 wsgi.py:
就是settings.py里的WSGI_APPLICATION配置,
一般运行Django项目时,runserver时使用Django自带的WSGI server去运行项目,需要获取一个WSGIServer对象,接受用户请求,
获取WSGIServer对象就是通过执行wsgi.py里的函数实现的

上诉是一开始就有的几个默认文件,还有些其他的比较重要的文件,如下:

#### 2.3.5 views.py:
处理用户发出的请求，从urls.py中对应过来,
通过渲染templates中的网页可以将显示内容,比如登陆后的用户名,用户请求的数据,输出到网页

#### 2.3.6 models.py:
与数据库操作相关,存入或读取数据时用到这个

#### 2.3.7 admin.py:
后台，可以用很少量的代码就拥有一个强大的后台

#### 2.3.8 forms.py:
表单,用户在浏览器上输入数据提交,对数据的验证工作以及输入框的生成等工作

#### 2.3.9 templates 文件夹:
views.py中的函数渲染templates中的Html模板，得到动态内容的网页