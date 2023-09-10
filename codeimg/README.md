# codeimg

一个可以将信息隐写到图片中的工具，当然也可以从具有隐写信息的图片中获取信息。

详情参考：[图中藏(cáng)语](https://blog.5km.studio/2018/10/20/codeimg-python/)

## 依赖

需要安装第三方库 **pillow**：

- 如果使用 pipenv 虚拟环境：

    ```sh
    $ pipenv pillow
    ```

- 如果适用系统的环境，直接使用 pip 安装即可：

    ```sh
    $ pip3 install pillow
    ```

## 使用

```sh
$ ./codeimg encode demo.png -i 'https://blog.5km.studio'
demo_code.png 已写入隐藏信息！
$ ./codeimg decode demo_code.png
解析到隐藏信息：https://blog.5km.studio
$ ./codeimg check demo.png
图片可用空间 381024 bytes
$ ./codeimg -h
usage: codeimg [-h] [-i INFO] {encode,decode,check} imgpath

为图片写入隐藏信息，或者从包含隐藏信息的图片中获取信息。

positional arguments:
  {encode,decode,check}
                        指定子命令。encode -> 往图片中写入隐藏信息；decode -> 读取图片中的隐藏信息；check
                        -> 查看图片可存空间(单位 byte)
  imgpath               指定要处理的图片

optional arguments:
  -h, --help            show this help message and exit
  -i INFO, --info INFO  指定要写入的隐藏信息，子命令为 encode 时有效
```
