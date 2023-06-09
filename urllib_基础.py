import urllib.request
# 定义一个url，即为我们要访问的地址
# url = "http://www.baidu.com"

# 模拟浏览器向服务器发送请求，response响应
# response = urllib.request.urlopen(url)

# 获取响应中的源码
# read方法，返回的是字节形式的二进制数据
# 我们需要将二进制数据转化为字符串
# 二进制->字符串  解码  decode('编码的格式')
# content = response.read().decode("utf-8")

# 打印数据
# print(content)

'''一个类型和六个方法'''
# response是HTTPResponse类型
# print(type(response))

# 按照一个字节一个字节地去读
# content = response.read()

# 返回多少个字节
# content = response.read(5)

# 只读取一行
# content = response.readline()
# print(content)

# 只读取全部行
# content = response.readlines()
# print(content)

# 返回状态码，如果是200，就证明逻辑没有错
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# 获取是一个状态信息
# print(response.getheaders())

'''urllib下载'''

# 下载网页
# urllib.request.urlretrieve(url, "filename_baidu.html")

# 下载图片
# url_image = "https://th.bing.com/th/id/OIP.qcaQpU5hEC9fQF73JECaTAHaEK?w=331&h=186&c=7&r=0&o=5&dpr=1.5&pid=1.7"
# urllib.request.urlretrieve(url_image, "宵宫.jpg")

# 下载视频
# url_video = "https://kvideo01.youju.sohu.com/a2f4319b-771d-4267-aa21-bdf4c4b826c72_0_0.mp4?sign=933baf65f935665bc2f5f64f7365356e&t=1685400322"
# urllib.request.urlretrieve(url_video, "video.mp4")

'''UA反爬，请求对象'''
# import urllib.request
#
# url = 'https://www.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.9'
# }
#
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf8')
#
# print(content)

'''get请求的quote方法'''
# import urllib.request
# import urllib.parse
# name = urllib.parse.quote('周杰伦') # 将中文转化为Unicode编码
# url = 'https://www.baidu.com/s?wd='
# url = url + name
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.9'
# }
#
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf8')
# print(content)

'''get请求的urlencode方法'''
# 有多个参数需要转化为Unicode编码
# https://www.baidu.com/s?wd=周杰伦&sex=男&location=中国台湾
import urllib.parse

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}
a = urllib.parse.urlencode(data)
url = 'https://www.baidu.com/s?'
url = url + a
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.9'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
