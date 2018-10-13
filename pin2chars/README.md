# douyin 

一个简单的验证码识别器，使用三种方法，前两种使用现成的库识别，后一种使用图像识别的方法自己实现。实现的验证码识别器有一定局限性，对于现在的验证码识别率低一些。此脚本主要是为了实践，熟悉python编程。

## 准备工作

所需库：

- pipenv
- pytesseract
- tesseract_ocr
- pillow

这里使用独立的python环境进行开发，用到了**pipenv**

1. 首先安装 **pipenv**

    ```sh
    pip3 install pipenv
    ```

2. 为当前工程激活独立的python环境：

    ```sh
    pipenv install
    ```

3. 进入pipenv的独立环境：

    ```sh
    pipenv shell
    ```

    进入后会看到命令行每条命令输入前多了一部分信息，形如`(pin2chars-E2eD5P-4)`

4. 在安装和使用库 **pytesseract** 和 **tesseract_ocr** 之前需要安装 **tesseract**：

    - macOS下：`brew install tesseract`
    - 其它系统，根据自己系统的包安装方法安装；

5. 然后使用 `pip3` 安装库（库会安装在当前的激活环境中）：

    ```sh
    pip3 install pipenv pytesseract tesseract_ocr pillow
    ```

### 提示

使用独立的python环境是因为不想在系统的python环境中安装一些东西，这样做不会影响系统的开发环境，使用独立的环境会使工程更具独立性！

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

详见[python3 简单实现验证码识别器](https://www.smslit.top/2018/10/12/verification_code_chars)
