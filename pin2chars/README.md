# pin2chars 

一个简单的验证码识别器，使用三种方法，前两种使用现成的库识别，后一种使用图像识别的方法自己实现。实现的验证码识别器有一定局限性，对于现在的验证码识别率低一些。此脚本主要是为了实践，熟悉python编程。

详情参考：[python3 简单实现验证码识别器](https://blog.5km.studio/2018/10/12/verification_code_chars/)
## 准备工作

所需库：

- pytesseract
- tesseract_ocr
- pillow

1. 在安装和使用库 **pytesseract** 和 **tesseract_ocr** 之前需要安装 **tesseract**：

    - macOS下：`brew install tesseract`
    - 其它系统，根据自己系统的包安装方法安装；

2. 安装库：

    - 如果使用 pipenv 虚拟环境：

        ```sh
        $ pipenv install pytesseract tesseract_ocr pillow
        ```

    - 如果适用系统的环境，直接使用 pip 安装即可：

        ```sh
        $ pip3 install pytesseract tesseract_ocr pillow
        ```

## 使用

```sh
$ ./pin2chars -h
usage: pin2chars [-h] [-m {0,1,2}] imgfile

positional arguments:
  imgfile               指定要识别的验证码图片

optional arguments:
  -h, --help            show this help message and exit
  -m {0,1,2}, --method {0,1,2}
                        选择方法进行验证码的识别: 0. 使用 pin_cracker 库方法识别验证码; 1. 使用
                        pytesseract 库方法识别验证码; 2. 使用 tesseract_ocr 库方法识别验证码;
```

## 思路

详见[python3 简单实现验证码识别器](https://blog.5km.studio/2018/10/12/verification_code_chars)
