# douyin 

使用python3为图片添加抖音效果，生成动态的抖音效果图。

详情参考：[python实现图片的抖音效果](https://www.smslit.top/2018/07/04/python-practice-douyin/)

## 依赖

- pillow
- numpy
- imageio

- 如果使用 pipenv 虚拟环境：

    ```sh
    $ pipenv install pillow numpy imageio
    ```

- 如果适用系统的环境，直接使用 pip 安装即可：

    ```sh
    pip3 install pillow numpy imageio
    ```

## 使用

将 [douyin.py](douyin.py) 中的 **PIC_PATH** 改成相应图片路径即可执行脚本：

```sh
python3 douyin.py
```