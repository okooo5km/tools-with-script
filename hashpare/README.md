# hashpare

一个文件校验工具，也可以通过校验比较两文件。

使用方法：

```Shell
$ ./hashpare -h
usage: hashpare [-h] {check,compare,calculate} ...

计算文件校验，检查校验值，比较两个文件

positional arguments:
  {check,compare,calculate}
                        子命令
    check               检查校验值命令
    compare             比较两个文件
    calculate           计算校验码

optional arguments:
  -h, --help            show this help message and exit
$ ./hashpare check -h
usage: hashpare check [-h] [-a {sha1,md5}] file hash

positional arguments:
  file                  指明文件路径
  hash                  指定校验码

optional arguments:
  -h, --help            show this help message and exit
  -a {sha1,md5}, --algorithm {sha1,md5}
                        指定校验算法
$ ./hashpare compare -h
usage: hashpare compare [-h] [-a {sha1,md5}] file file

positional arguments:
  file                  指定要比较的两个文件

optional arguments:
  -h, --help            show this help message and exit
  -a {sha1,md5}, --algorithm {sha1,md5}
                        指定校验算法
$ ./hashpare calculate -h
usage: hashpare calculate [-h] [-a {sha1,md5}] file [file ...]

positional arguments:
  file                  指定要计算校验的文件

optional arguments:
  -h, --help            show this help message and exit
  -a {sha1,md5}, --algorithm {sha1,md5}
                        指定校验算法
```