# img2ascii

此脚本工具可以将图片转换为字符画。

详情参考：[python3实现图片转换为字符画](https://blog.5km.studio/2018/09/14/image2charspic/)

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

示例图片：

![https://blog.5km.studio/android-chrome-512x512.png](https://blog.5km.studio/android-chrome-512x512.png)

```
$ ./img2ascii android-chrome-512x512.png -W 20 -H 20
```

得到 **output.txt**，内容对应的效果如下：

![20180914153693707997013.png](http://p9fh104m8.bkt.clouddn.com/20180914153693707997013.png)