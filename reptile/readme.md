爬虫相关的项目都用同一个虚拟环境
虚拟环境安装在PythonLearing/reptile目录下
虚拟环境安装参考:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000

通常是你的项目所在目录下,执行:
```
virtualenv --no-site-packages venv
```
则创建了一个不带第三方方库的干净的虚拟python环境

然后执行source venv/bin/activate  切换成该虚拟环境
然后开始编程吧,需要什么库就去下载什么库

比如 import requests,就会报错.说找不到这个名字的模块,因为我们新建的虚拟环境里没有这个库.
去下载一个就好了
基本上执行pip install 库名  就可以下载了

然而执行pip install requests竟然报错了,
Could not find a version that satisfies the requirement urllib3 (from versions: )No matching distribution found for urllib3
原因:https://blog.csdn.net/iaiti/article/details/49613097
解决办法参考:
https://stackoverflow.com/questions/29099404/ssl-insecureplatform-error-when-using-requests-package
https://blog.bbzhh.com/index.php/archives/111.htmlop
执行 pip install 'requests[security]'  依旧报错

后来执行了一下easy_install requests ,发现去以前公司的一个内部地址去下载requests库了... 难怪一直失败...
修改了pip下载源地址以后,就好了...
pip配置文件路径:  ~/.pip下的pip.conf