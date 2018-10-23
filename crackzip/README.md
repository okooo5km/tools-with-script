# crackzip

破解 zip 文件密码的工具。

## 库

使用 python 内建库 `zipfile`

## 使用

```sh
$ ./crackzip -h
usage: crackzip [-h] zfile dict

暴力破解 zip 文件的密码

positional arguments:
  zfile       指明要破解的 zip 文件，可以是多个
  dict        指定使用的密码词典

optional arguments:
  -h, --help  show this help message and exit
$ ./crackzip demo.zip keys.dict
[+] 密码是 6556 [+]
$ ./crackzip demo1.zip keys.dict
demo1.zip 未加密！
```