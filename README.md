# tools-with-script

用脚本编写的工具整理。

## 准备工作

为了使工具集使用的第三方库几环境变量独立于系统环境，这里使用 pipenv 创建虚拟的 python开发环境。

1. 安装 pipenv:

    ```sh
    $ pip3 install pipenv
    ```

2. 创建虚拟环境：

    ```sh
    # pipenv install --three
    $ pipenv install --python 3
    ```

3. 因为有 `Pipfile` 和 `Pipfile.lock` 文件，所以可以同步安装需要的第三方包：

    ```sh
    $ pipenv sync
    ```

### 提示

使用独立的 python 环境是因为不想在系统的 python 环境中安装一些东西，这样做不会影响系统的开发环境，使用独立的环境会使工程更具独立性！关于 pipenv 的使用可以参考：[一起使用 pipenv](https://www.smslit.top/2018/10/18/pipenv/)

## 工具集

### douyin

[douyin](douyin/douyin.py) 是python3实现的可以为图片添加抖音效果，同时生成动态抖音效果图的工具。

### hexo2hugo

[hexo2hugo](hexo2hugo/hexo2hugo.py) 是用于转换hexo源文章头信息为hugo格式的工具。

### img2ascii

[img2ascii](img2ascii/img2ascii) 是可以将图片转换为字符画的工具。

### pin2chars

[pin2chars](pin2chars/pin2chars) 是一个简单的验证码识别器。

### m2h

[m2h](m2h/m2h) 是一个将 markdown 文件转换为 html 文件的工具

### csv2xls

[csv2xls](csv2xls/csv2xls) 是一个将 csv 转换为 xls 文件的工具。

### codeimg

[codeimg](codeimg/codeimg) 是一个可以将信息隐写到图片中的工具，当然也可以从具有隐写信息的图片中获取信息。