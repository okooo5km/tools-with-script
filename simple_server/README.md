# simple_server

一个支持 HTTP/1.1 长连接的单进程、单线程、非阻塞的静态服务器。

# 使用方法

```Shell
$ ./simple_server -h
usage: simple_server [-h] [-p PORT] site

开启指定网站服务

positional arguments:
  site                  指定网站路径

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  指定网服务端口
```
