# m2h

一个将 markdown 文件转换为 html 文件的工具。

详情参考：[python3 实现Markdown转html小工具](https://www.smslit.top/2018/10/16/md2html_python/)

## 依赖

需要安装第三方库：

- 如果使用 pipenv 虚拟环境：

  ```sh
  $ pipenv install markdown beautifulsoup4 html5lib
  ```

- 如果适用系统的环境，直接使用 pip 安装即可：

  ```sh
  $ pip3 install markdown beautifulsoup4 html5lib
  ```

## 使用

```sh
$ ./m2h -h
usage: m2h [-h] [-s STYLE] [-o OUTDIR] infiles [infiles ...]

positional arguments:
  infiles               指定要转换的 markdown 文件，可以指定多个

optional arguments:
  -h, --help            show this help message and exit
  -s STYLE, --style STYLE
                        指定要使用的 css 样式，css文件路径
  -o OUTDIR, --outdir OUTDIR
                        指定 html 文件输出目录
```
