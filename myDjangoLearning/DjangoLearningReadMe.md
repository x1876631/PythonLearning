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

<br/>

## 3.Django的运作过程:
### 3.1.Django开始运行:
先加载Django的settings,再创建WSGIServer实例,调用serve_forever()方法启动http服务

### 3.2.Django处理请求的流程:
* 1.用户通过浏览器请求一个页面
* 2.请求到达RequestMiddlewares,中间件对request预处理或者直接response
* 3.预处理以后URLConf通过urls.py文件和request里的url找到相应的view
* 4.ViewMiddlewares被访问,同样可以对request做预处理或者直接response
* 5.调用view的函数
* 6.View可以通过models访问底层的数据,model和db的交互都是通过manager
* 7.如何需要,views可以使用一个特殊的context传给template生成页面,然后再把输出返回给view
* 8.httpResponse被发送回到ResponseMiddlewares
* 9.response被返回给浏览器,将结果呈现给用户

### 3.3.流程重点部分解析:
#### 3.3.1. Middleware(中间件)
middleware可以参数的阶段有4个:reqeust/view/response/exception<br/>
中间件在settings.py的MIDDLEWARE_CLASSES定义,使用完整的python类路径,中间件可以为空<br/>
中间件的配置顺序很重要,从request到view的顺序调用的,而exception和response是逆序调用的
<br/>

#### 3.3.2. URLConf(URL映射)
如果处理request的中间件都没有返回response,那么Django回去解析用户请求的url.<br/>
URLConf是Django网站的目录,是url和view之间的映射表,以便Django能知道哪个url要调用哪段代码.<br/>
具体配置在settings.py文件的ROOT_URLCONF常量里配置

#### 3.3.2. Template(模板)
非python代码实现,而是通过filter和template tag实现<br/>
