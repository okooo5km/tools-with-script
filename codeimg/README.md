# codeimg

一个可以将信息隐写到图片中的工具，当然也可以从具有隐写信息的图片中获取信息。

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
$ ./codeimg -h
usage: codeimg [-h] [-i INFO] imgpath

为图片写入隐藏信息，或者从包含隐藏信息的图片中获取信息。

positional arguments:
  imgpath               指定要处理的图片

optional arguments:
  -h, --help            show this help message and exit
  -i INFO, --info INFO  指定要写入的隐藏信息，若指定会向图片写入信息，若不指定会尝试读取图片中的隐藏信息
```
