# coding=utf-8
import urllib

# 请求百度首页
response = urllib.urlopen('http://www.baidu.com/')

# 输出本次请求结果的状态码
print(response.code)

# 输出获取的响应结果，是个网页
print(response.read())
