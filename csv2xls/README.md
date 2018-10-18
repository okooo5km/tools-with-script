# csv2xls

是一个将 csv 转换为 xls 文件的工具，可批量转换。

## 第三方库

- xlwt

安装：

- 如果使用 pipenv 虚拟环境：

    ```sh
    $ pipenv install xlwt
    ```

- 如果适用系统的环境，直接使用 pip 安装即可：

    ```sh
    $ pip3 install xlwt
    ```

## 使用

```sh
$ csv2xls/csv2xls -h
usage: csv2xls [-h] paths [paths ...]

转换单个 csv 文件，或转换指定目录下的所有 csv 文件

positional arguments:
  paths       指定一个或多个路径，可以是csv文件，也可以是一个目录的路径

optional arguments:
  -h, --help  show this help message and exit
```

1. 直接转换指定 csv 文件，最终在同级目录生成 xls 文件：

```sh
$ ./csv2xls demo.csv demo2.csv
```

2. 转换指定目录下的所有 csv 文件：

```sh
$ ./csv2xls demodir1 demodir2
```
