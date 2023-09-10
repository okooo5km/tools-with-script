# tee

python实现的 tee 命令。

详情参考：[python 实现命令行工具 tee](https://blog.5km.studio/2018/10/12/tee-Python/)

使用方法:

```Shell
$ ./tee -h
usage: tee [-h] [-v] [-a] [file [file ...]]

The tee utility copies standard input to standard output, making a copy in
zero or more files. The output is unbuffered.

positional arguments:
  file           A pathname of an output file.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -a, --append   Append the output to the files rather than overwriting them.
```