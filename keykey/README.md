# keykey

这是一个密码字典生成器。

详情参考：[python3 生成密码字典](https://blog.5km.studio/2018/10/21/unzip-dict-hacker/)

使用方法：

```sh
$  ./keykey -h
usage: keykey [-h] [-o OUTFILE] [-c CHOICES] minlength maxlength

用于生成指定长度和字符空间的密码字典

positional arguments:
  minlength             用于指定生成密码的最小位数
  maxlength             用于指定生成密码的最大位数

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        指定字典文件的保存路径
  -c CHOICES, --choices CHOICES
                        指定字符串，密码中的字符从字符串中选择，默认为 "0123456789"
$ ./keykey 4 6
[+] 已生成 4 ~ 6 位密码字典 [+]
[+] 已保存密码字典到 /Users/5km/Desktop/keys.txt [+]
$ head -n 5 /Users/5km/Desktop/keys.txt
0000
0001
0002
0003
0004
$ ./keykey 4 6 -o keys.txt
[+] 已生成 4 ~ 6 位密码字典 [+]
[+] 已保存密码字典到 /Users/5km/Documents/workspace/python/tools-with-script/keykey/keys.txt [+]
$ head -n 5 keys.txt
0000
0001
0002
0003
0004
$ ./keykey 4 6 -o keys.txt -c 'asdfghjkl'
[+] 已生成 4 ~ 6 位密码字典 [+]
[+] 已保存密码字典到 /Users/5km/Documents/workspace/python/tools-with-script/keykey/keys.txt [+]
$ head -n 5 keys.txt
aaaa
aaas
aaad
aaaf
aaag
```