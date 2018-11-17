# qdownload

批量下载七牛云文件的工具。

## 依赖

- 如果使用 pipenv 虚拟环境：

    ```sh
    $ pipenv install requests
    ```

- 如果适用系统的环境，直接使用 pip 安装即可：

    ```sh
    $ pip3 install requests
    ```

## 使用

```shell
$ ./qdownload -h
usage: qdownload [-h] [-o OUTDIR] domain infile

批量下载七牛云中的文件

positional arguments:
  domain                指定七牛 bucket 的CDN域名
  infile                指定七牛 bucket 中文件对应的列表文件

optional arguments:
  -h, --help            show this help message and exit
  -o OUTDIR, --outdir OUTDIR
                        指定要新建的目录，用于存储文件，最终存储目录为 ~/Downloads/[outdir]
```

1. 七牛 bucket 的CDN域名

    访问七牛云，在自己创建的对象存储的页面就会看到一个测试用的 CDN 域名，如果自己已经指定为其他的 CDN 域名，使用指定的 CDN 域名即可

2. 文件列表获取

    使用七牛云提供的 [qshell](https://developer.qiniu.com/kodo/tools/1302/qshell) 命令行工具获取。

    - 下载后解压，会看到对应自己系统版本的 qshell，比如 macOS 下使用的是 `qshell_darwin_x64`，为了方便调用建立一个软连接：

        ```Shell
        ln -s qshell_darwin_x64 qshell
        ```

    - 登录账户

        ```Shell
        ./qshell account <AK> <SK> <username>
        ```

        - <AK> 是 app key （个人中心->密钥管理中查看）
        - <SK> 是 secret key （个人中心->密钥管理中查看）
        - <username> 是你的七牛账户名

    - 获取文件详细列表：

        ```Shell
        ./qshell listbucket <bucket> > filelist.txt
        ```

        - <bucket> 是要操作的对象空间的名称

    - 切分出文件名称的列表：

        ```Shell
        cat filelist.txt | awk -F '\t' '{print $1}' > list.txt
        ```

    `list.txt` 就是七牛云 bucket 中文件对应的列表文件
